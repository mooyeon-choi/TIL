const GLOBE_RADIUS = 0.7;
const FIELD_OF_VIEW = 0.8;
const DOT_RADIUS = 4;
const PI2 = Math.PI * 2;

export class Dot {
  constructor(x, y, z, stageWidth, stageHeight) {
    this.centerX = stageWidth / 2;
    this.centerY = stageHeight / 2;
    this.centerZ = stageHeight * -GLOBE_RADIUS;

    this.stageWidth = stageWidth;
    this.stageHeight = stageHeight;

    this.x = x;
    this.y = y;
    this.z = z;

    this.xProject = 0;
    this.yProject = 0;
    this.sizeProjection = 0;
  }

  resize(stageWidth, stageHeight) {
    this.stageWidth = stageWidth;
    this.stageHeight = stageHeight;

    this.centerX = stageWidth / 2;
    this.centerY = stageHeight / 2;
    this.centerZ = stageHeight * -GLOBE_RADIUS;
  }

  // Project our element from its 3D world to the 2D canvas
  project(sin, cos) {
    const rotX = cos * this.x + sin * (this.z - this.centerZ);
    const rotZ = -sin * this.x + cos * (this.z - this.centerZ) + this.centerZ;
    this.sizeProjection =
      (this.stageHeight * FIELD_OF_VIEW) /
      (this.stageHeight * FIELD_OF_VIEW - rotZ);
    this.xProject = rotX * this.sizeProjection + this.centerX;
    this.yProject = this.y * this.sizeProjection + this.centerY;
  }

  animate(ctx, sin, cos) {
    this.project(sin, cos);

    ctx.beginPath();
    ctx.fillStyle = `#f4e55a`;
    ctx.arc(
      this.xProject,
      this.yProject,
      DOT_RADIUS * this.sizeProjection,
      0,
      PI2
    );
    ctx.closePath();
    ctx.fill();
  }
}
