import { Cube } from "./cube.js";
import { Point2D } from "./utils.js";

class App {
  constructor() {
    this.canvas = document.createElement("canvas");
    document.body.appendChild(this.canvas);
    this.ctx = this.canvas.getContext("2d");

    this.pixelRatio = window.divicePixelRatio > 1 ? 2 : 1;

    this.pointer = new Point2D(0, 0);
    this.startPos = new Point2D(0, 0);
    this.endPos = new Point2D(0, 0);

    this.cube = new Cube(0, 0, 400, 200);

    window.addEventListener("resize", this.resize.bind(this), false);
    this.resize();

    window.requestAnimationFrame(this.animate.bind(this));

    document.addEventListener("pointerdown", this.onDown.bind(this), false);
    document.addEventListener("pointerup", this.onUp.bind(this), false);
  }

  resize() {
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.canvas.width = this.stageWidth * this.pixelRatio;
    this.canvas.height = this.stageHeight * this.pixelRatio;
    this.ctx.scale(this.pixelRatio, this.pixelRatio);
  }

  animate() {
    window.requestAnimationFrame(this.animate.bind(this));

    this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

    this.cube.rotateX(this.pointer.y * 0.0001);
    this.cube.rotateY(-this.pointer.x * 0.0001);

    this.cube.animate(this.ctx, this.stageWidth, this.stageHeight);
  }

  onDown(e) {
    this.startPos.x = e.clientX;
    this.startPos.y = e.clientY;
    this.startTime = Date.now();
  }

  onUp(e) {
    this.endTime = Date.now();
    this.endPos.x = e.clientX;
    this.endPos.y = e.clientY;

    this.pointer.x =
      ((this.endPos.x - this.startPos.x) / (this.endTime - this.startTime)) *
      200;

    this.pointer.y =
      ((this.endPos.y - this.startPos.y) / (this.endTime - this.startTime)) *
      200;
  }
}

window.onload = () => {
  new App();
};
