"use strict";
console.log("app is running!");

class App {
  constructor() {
    this.app = document.createElement("div");
    this.app.id = "app";
    document.body.appendChild(this.app);

    this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1;

    this.carousel = new Carousel(this.app);

    window.addEventListener("resize", this.resize.bind(this), false);
    this.resize();
  }

  resize() {
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.app.width = this.stageWidth * this.pixelRatio;
    this.app.height = this.stageHeight * this.pixelRatio;
  }
}

window.onload = () => {
  new App();
};
