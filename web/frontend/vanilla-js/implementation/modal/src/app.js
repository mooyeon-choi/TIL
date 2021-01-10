"use strict";
console.log("app is running!");

class App {
  $target = null;

  constructor($target) {
    this.$target = $target;

    console.log(this.$target);
    const button = document.createElement("button");
    button.addEventListener("click", this.onOpenModal.bind(this), false);
    button.innerText = "Click!";
    $target.appendChild(button);

    this.info = new Modal({
      $target,
      visible: false,
    });
  }

  onOpenModal() {
    this.info.setState();
  }
}

window.onload = () => {
  new App(document.querySelector("#App"));
};
