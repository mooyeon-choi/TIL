"use strict";
console.log("app is running!");

import { Carousel } from "./carousel.js";

class App {
  constructor() {
    this.app = document.createElement("div");
    document.body.appendChild(this.app);

    this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1;

    this.carousel = new Carousel();

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
