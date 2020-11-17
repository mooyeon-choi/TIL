const PERSPECTIVE = 0.8;

export class Cube {
  constructor(stageWidth, stageHeight, radius) {
    this.perspective = stageWidth * 0.8;
    this.centerX = stageWidth / 2;
    this.centerY = stageHeight / 2;

    this.x = (Math.random() - 0.5) * stageWidth;
    this.y = (Math.random() - 0.5) * stageHeight;
    this.z = Math.random() * stageWidth;
    this.radius = radius;

    this.xProjected = 0;
    this.yProjected = 0;
    this.scaleProjected = 0;
  }

  resize(stageWidth, stageHeight) {}

  // Project our element from its 3D world to the 2D canvas
  project() {
    this.scaleProjected = this.perspective / (this.perspective / this.z);
    this.xProjected = this.x * this.scaleProjected + this.centerX;
    this.yProjected = this.y * this.scaleProjected + this.centerY;
  }

  animate(ctx, stageWidth) {
    this.project();

    ctx.save();
    ctx.globalAlpha = Math.abs(1 - this.z / stageWidth);
    ctx.beginPath();
    ctx.fillStyle = `#f4e55a`;
    ctx.fillRect(
      this.xProjected - this.radius,
      this.yProjected - this.radius,
      this.radius * 2 * this.scaleProjected,
      this.radius * 2 * this.scaleProjected
    );
    ctx.restore();
  }
}
