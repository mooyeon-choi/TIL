import { Text } from "./text.js";

class App {
  constructor() {
    WebFont.load({
      google: {
        families: ["Hind:700"],
      },
      fontactive: () => {
        this.text = new Text();
        this.text.setText(
          "T",
          2,
          document.body.clientWidth,
          document.body.clientHeight
        );
      },
    });
  }
}

window.onload = () => {
  new App();
};
