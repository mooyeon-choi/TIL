import { Text } from "./text.js";
import { Particle } from "./particle.js";

export const RANDOM_TEXT = "ABCMNRSTUXZ";

export class Visual {
  constructor() {
    this.text = new Text();

    this.textArr = RANDOM_TEXT.split("");

    this.particles = [];

    this.mouse = {
      x: 0,
      y: 0,
      radius: 100,
    };

    document.addEventListener("pointermove", this.onMove.bind(this), false);
    document.addEventListener("touchmove", this.onTouchMove.bind(this), false);
  }

  show(stageWidth, stageHeight) {
    const fontSize = stageWidth > 700 ? 14 : 10;
    const fontWidth = stageWidth > 700 ? 26 : 19;

    const str = this.textArr[
      Math.round(Math.random() * (this.textArr.length - 1))
    ];
    this.pos = this.text.setText(str, fontWidth, stageWidth, stageHeight);

    this.particles = [];
    for (let i = 0; i < this.pos.length; i++) {
      const item = new Particle(this.pos[i], fontSize);
      this.particles.push(item);
    }
  }

  animate(ctx, t) {
    for (let i = 0; i < this.particles.length; i++) {
      const item = this.particles[i];

      const dx = this.mouse.x - item.x;
      const dy = this.mouse.y - item.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      const minDist = item.radius + this.mouse.radius;

      if (dist < minDist) {
        const angle = Math.atan2(dy, dx);
        const tx = item.x + Math.cos(angle) * minDist;
        const ty = item.y + Math.sin(angle) * minDist;
        const ax = tx - this.mouse.x;
        const ay = ty - this.mouse.y;
        item.vx -= ax;
        item.vy -= ay;
        item.collide();
      }

      item.draw(ctx, t);
    }
  }

  onMove(e) {
    this.mouse.x = e.clientX;
    this.mouse.y = e.clientY;
  }

  onTouchMove(e) {
    this.mouse.x = e.touches[0].clientX;
    this.mouse.y = e.touches[0].clientY;
  }
}
