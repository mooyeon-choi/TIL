import { Dot } from "./dot.js";

class App {
  constructor() {
    console.log(arguments);
    this.canvas = document.createElement("canvas");
    document.body.appendChild(this.canvas);
    this.ctx = this.canvas.getContext("2d");

    this.pixelRatio = window.divicePixelRatio > 1 ? 2 : 1;

    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;
    this.rotating = 0;
    this.dots = [];
    this.total = 1000;
    for (let i = 0; i < this.total; i++) {
      const theta = Math.random() * 2 * Math.PI;
      const phi = Math.acos(Math.random() * 2 - 1);

      const globeRadius = this.stageHeight * 0.7;
      const x = globeRadius * Math.sin(phi) * Math.cos(theta);
      const y = globeRadius * Math.sin(phi) * Math.sin(theta);
      const z = globeRadius * Math.cos(phi) + this.stageHeight * -0.7;
      this.dots[i] = new Dot(x, y, z, this.stageWidth, this.stageHeight);
    }

    window.addEventListener("resize", this.resize.bind(this), false);
    this.resize();

    window.requestAnimationFrame(this.animate.bind(this));
  }

  resize() {
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.canvas.width = this.stageWidth * this.pixelRatio;
    this.canvas.height = this.stageHeight * this.pixelRatio;
    this.ctx.scale(this.pixelRatio, this.pixelRatio);

    for (let i = 0; i < this.dots.length; i++) {
      this.dots[i].resize(this.stageWidth, this.stageHeight);
    }
  }

  animate() {
    window.requestAnimationFrame(this.animate.bind(this));

    this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

    const rotation = arguments[0] * 0.0004;

    const sineRotation = Math.sin(rotation);
    const cosineRotation = Math.cos(rotation);

    for (let i = 0; i < this.dots.length; i++) {
      this.dots[i].animate(this.ctx, sineRotation, cosineRotation);
    }
  }
}

window.onload = () => {
  new App();
};
