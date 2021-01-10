class Modal {
  $info = null;

  constructor({ $target, visible }) {
    const $info = document.createElement("div");
    $info.className = "modalInfo";
    this.$info = $info;
    $target.appendChild($info);

    this.visible = visible;

    this.render();
  }

  setState(changeVisible) {
    this.visible = changeVisible;
    this.render();
  }

  closeInfo() {
    this.visible = false;
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
            <button class="close" onClick="${this.closeInfo}">x</button>
          </header>
          <img src="${src}" alt="image"/>
          <ul class="description">
            <li>첫번째</li>
            <li>두번째</li>
          </ul>
        </article>`;
      this.$info.style.display = "block";
    } else {
      this.$info.style.display = "none";
    }
  }
}
