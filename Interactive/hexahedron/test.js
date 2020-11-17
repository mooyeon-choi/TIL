console.clear();

// Get the canvas element from the DOM
const canvas = document.querySelector("#scene");
canvas.width = canvas.clientWidth;
canvas.height = canvas.clientHeight;
// Store the 2D context
const ctx = canvas.getContext("2d");

if (window.devicePixelRatio > 1) {
  canvas.width = canvas.clientWidth * 2;
  canvas.height = canvas.clientHeight * 2;
  ctx.scale(2, 2);
}

/* ====================== */
/* ====== VARIABLES ===== */
/* ====================== */
let width = canvas.clientWidth; // Width of the canvas
let height = canvas.clientHeight; // Height of the canvas
const dots = []; // Every dots in an array

/* ====================== */
/* ====== CONSTANTS ===== */
/* ====================== */
/* Some of those constants may change if the user resizes their screen but I still strongly believe they belong to the Constants part of the variables */
const DOTS_AMOUNT = 1000; // Amount of dots on the screen
const DOT_RADIUS = 2; // Radius of the dots
let PROJECTION_CENTER_X = width / 2; // X center of the canvas HTML
let PROJECTION_CENTER_Y = height / 2; // Y center of the canvas HTML
let FIELD_OF_VIEW = width * 0.8;
const CUBE_LINES = [
  [0, 1],
  [1, 3],
  [3, 2],
  [2, 0],
  [2, 6],
  [3, 7],
  [0, 4],
  [1, 5],
  [6, 7],
  [6, 4],
  [7, 5],
  [4, 5],
];
const CUBE_VERTICES = [
  [-1, -1, -1],
  [1, -1, -1],
  [-1, 1, -1],
  [1, 1, -1],
  [-1, -1, 1],
  [1, -1, 1],
  [-1, 1, 1],
  [1, 1, 1],
];

class Cube {
  constructor(x, y, z) {
    this.x = (Math.random() - 0.5) * width;
    this.y = (Math.random() - 0.5) * width;
    this.z = (Math.random() - 0.5) * width;
    this.radius = Math.floor(Math.random() * 12 + 10);

    TweenMax.to(this, Math.random() * 20 + 15, {
      x: (Math.random() - 0.5) * (width * 0.5),
      y: (Math.random() - 0.5) * (width * 0.5),
      z: (Math.random() - 0.5) * width,
      repeat: -1,
      yoyo: true,
      ease: Power2.EaseOut,
      delay: Math.random() * -35,
    });
  }
  // Do some math to project the 3D position into the 2D canvas
  project(x, y, z) {
    const sizeProjection = FIELD_OF_VIEW / (FIELD_OF_VIEW + z);
    const xProject = x * sizeProjection + PROJECTION_CENTER_X;
    const yProject = y * sizeProjection + PROJECTION_CENTER_Y;
    return {
      size: sizeProjection,
      x: xProject,
      y: yProject,
    };
  }
  // Draw the dot on the canvas
  draw() {
    // Do not render a cube that is in front of the camera
    if (this.z < -FIELD_OF_VIEW + this.radius) {
      return;
    }
    for (let i = 0; i < CUBE_LINES.length; i++) {
      const v1 = {
        x: this.x + this.radius * CUBE_VERTICES[CUBE_LINES[i][0]][0],
        y: this.y + this.radius * CUBE_VERTICES[CUBE_LINES[i][0]][1],
        z: this.z + this.radius * CUBE_VERTICES[CUBE_LINES[i][0]][2],
      };
      const v2 = {
        x: this.x + this.radius * CUBE_VERTICES[CUBE_LINES[i][1]][0],
        y: this.y + this.radius * CUBE_VERTICES[CUBE_LINES[i][1]][1],
        z: this.z + this.radius * CUBE_VERTICES[CUBE_LINES[i][1]][2],
      };
      const v1Project = this.project(v1.x, v1.y, v1.z);
      const v2Project = this.project(v2.x, v2.y, v2.z);
      ctx.beginPath();
      ctx.moveTo(v1Project.x, v1Project.y);
      ctx.lineTo(v2Project.x, v2Project.y);
      ctx.stroke();
    }
    // ctx.globalAlpha = Math.abs(this.z / (width * 0.5));
  }
}

function createDots() {
  // Empty the array of dots
  dots.length = 0;

  // Create a new dot based on the amount needed
  for (let i = 0; i < 100; i++) {
    dots.push(new Cube());
  }
}

/* ====================== */
/* ======== RENDER ====== */
/* ====================== */
function render() {
  // Clear the scene
  ctx.clearRect(0, 0, width, height);

  // Loop through the dots array and draw every dot
  for (var i = 0; i < dots.length; i++) {
    dots[i].draw();
  }

  window.requestAnimationFrame(render);
}

// Function called after the user resized its screen
function afterResize() {
  width = canvas.offsetWidth;
  height = canvas.offsetHeight;
  if (window.devicePixelRatio > 1) {
    canvas.width = canvas.clientWidth * 2;
    canvas.height = canvas.clientHeight * 2;
    ctx.scale(2, 2);
  } else {
    canvas.width = width;
    canvas.height = height;
  }
  PROJECTION_CENTER_X = width / 2;
  PROJECTION_CENTER_Y = height / 2;
  FIELD_OF_VIEW = width * 0.8;

  createDots(); // Reset all dots
}

// Variable used to store a timeout when user resized its screen
let resizeTimeout;
// Function called right after user resized its screen
function onResize() {
  // Clear the timeout variable
  resizeTimeout = window.clearTimeout(resizeTimeout);
  // Store a new timeout to avoid calling afterResize for every resize event
  resizeTimeout = window.setTimeout(afterResize, 500);
}
window.addEventListener("resize", onResize);

// Populate the dots array with random dots
createDots();

// Render the scene
window.requestAnimationFrame(render);
