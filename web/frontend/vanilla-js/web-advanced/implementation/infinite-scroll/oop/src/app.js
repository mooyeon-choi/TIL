"use strict";
console.log("app is running!");

class App {
  $target = null;
  data = null;

  constructor($target) {
    this.$target = $target;

    // this.data = () => {
    //   api.then(({ data }) => this.setState(data));
    // };

    document.body.addEventListener("click", this.onLoad.bind(this), false);
  }

  onLoad() {
    api.fetchCats().then((data) => this.setState(data));
  }

  setState(nextData) {
    this.data = nextData;
    console.log(nextData);
  }
}
