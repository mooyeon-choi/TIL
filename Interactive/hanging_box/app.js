import { Point } from "./point.js";
import { Dialog } from "./dialog.js";

class App {
  constructor() {
    this.canvas = document.createElement("canvas");
    document.body.appendChild(this.canvas);
    this.ctx = this.canvas.getContext("2d");

    this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1;

    window.addEventListener("resize", this.resize.bind(this), false);
    this.resize();

    window.requestAnimationFrame(this.animate.bind(this));

    this.mousePos = new Point();
    this.curItem = null;

    this.items = [];
    this.total = 1;
    for (let i = 0; i < this.total; i++) {
      this.items[i] = new Dialog();
    }

    document.addEventListener("pointerdown", this.onDown.bind(this), false);
    document.addEventListener("pointermove", this.onMove.bind(this), false);
    document.addEventListener("pointerup", this.onUp.bind(this), false);
  }

  resize() {
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.canvas.width = this.stageWidth * this.pixelRatio;
    this.canvas.height = this.stageHeight * this.pixelRatio;
    this.ctx.scale(this.pixelRatio, this.pixelRatio);

    this.ctx.shadowOffsetX = 0;
    this.ctx.shadowOffsetY = 3;
    this.ctx.shadowBlur = 6;
    this.ctx.shadowColor = `rgba(0, 0, 0, 0.1)`;

    this.ctx.lineWidth = 2;

    for (let i = 0; i < this.items.length; i++) {
      this.items[i].resize(this.stageWidth, this.stageHeight);
    }
  }

  animate() {
    window.requestAnimationFrame(this.animate.bind(this));

    this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

    for (let i = 0; i < this.items.length; i++) {
      console.log(this.items[i]);
      this.items[i].animate(this.ctx);
    }
  }

  onDown(e) {
    this.mousePos.x = e.clientX;
    this.mousePos.y = e.clientY;

    for (let i = this.items.length - 1; i >= 0; i--) {
      const item = this.items[i].down(this.mousePos.clone());
      if (item) {
        this.curItem = item;
        const index = this.items.indexOf(item);
        this.items.push(this.items.splice(index, 1)[0]);
        break;
      }
    }
  }

  onMove(e) {
    this.mousePos.x = e.clientX;
    this.mousePos.y = e.clientY;
  }

  onUp(e) {}
}

window.onload = () => {
  new App();
};
