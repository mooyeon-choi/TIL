"use strict";
console.log("modal is running!");

class Modal {
  $info = null;

  constructor({ $target, visible }) {
    const $info = document.createElement("div");
    $info.className = "modal-info";
    this.$info = $info;
    $target.appendChild($info);

    this.visible = visible;

    this.render();
  }

  setState() {
    this.visible = !this.visible;
    this.render();
  }

  closeInfo() {
    this.visible = false;
    this.$info.style.animation = "fadeout 2s";
    this.render();
  }

  render() {
    const src =
      "https://github.com/mooyeon-choi/kinetic-typography-6/raw/main/images/kinetic-typography-6-example.gif";
    if (this.visible) {
      this.$info.innerHTML = `
        <article class="content-wrapper">
          <header class="title">
            <span>제목</span>
            <button class="close">x</button>
          </header>
          <img src="${src}" alt="image"/>
          <ul class="description">
            <li>첫번째</li>
            <li>두번째</li>
          </ul>
        </article>`;

      const closeModal = this.$info.querySelector(".close");
      closeModal.addEventListener("click", this.closeInfo.bind(this), false);

      this.$info.style.display = "block";
    } else {
      this.$info.style.display = "none";
    }
  }
}
