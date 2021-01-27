"use strict";
console.log("carousel is running!");

class Carousel {
  $info = null;

  constructor($target) {
    const $info = document.createElement("div");
    $info.className = "carousel-box";
    this.$info = $info;
    $target.appendChild($info);
  }
}
