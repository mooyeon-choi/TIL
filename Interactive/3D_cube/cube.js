import { Point2D, Point3D } from "./utils.js";

export class Cube {
  constructor(x, y, z, size) {
    Point3D.call(this, x, y, z);

    size *= 0.5;

    this.vertices = [
      new Point3D(x - size, y - size, z - size),
      new Point3D(x + size, y - size, z - size),
      new Point3D(x + size, y + size, z - size),
      new Point3D(x - size, y + size, z - size),
      new Point3D(x - size, y - size, z + size),
      new Point3D(x + size, y - size, z + size),
      new Point3D(x + size, y + size, z + size),
      new Point3D(x - size, y + size, z + size),
    ];

    this.faces = [
      [0, 1, 2, 3],
      [0, 4, 5, 1],
      [1, 5, 6, 2],
      [3, 2, 6, 7],
      [0, 3, 7, 4],
      [4, 7, 6, 5],
    ];
  }

  resize(stageWidth, stageHeight) {}

  // Project our element from its 3D world to the 2D canvas
  project(points3d, stageWidth, stageHeight) {
    const points2d = new Array(points3d.length);

    const focal_length = 200;

    for (let index = points3d.length - 1; index > -1; --index) {
      const p = points3d[index];

      const x = p.x * (focal_length / p.z) + stageWidth * 0.5;
      const y = p.y * (focal_length / p.z) + stageHeight * 0.5;

      points2d[index] = new Point2D(x, y);
    }

    return points2d;
  }

  animate(ctx, stageWidth, stageHeight) {
    const vertices = this.project(this.vertices, stageWidth, stageHeight);

    for (let index = this.faces.length - 1; index > -1; --index) {
      const face = this.faces[index];

      const p1 = this.vertices[face[0]];
      const p2 = this.vertices[face[1]];
      const p3 = this.vertices[face[2]];

      const v1 = new Point3D(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z);
      const v2 = new Point3D(p3.x - p1.x, p3.y - p1.y, p3.z - p1.z);

      const n = new Point3D(
        v1.y * v2.z - v1.z * v2.y,
        v1.z * v2.x - v1.x * v2.z,
        v1.x * v2.y - v1.y * v2.x
      );

      if (-p1.x * n.x + -p1.y * n.y + -p1.z * n.z <= 0) {
        ctx.beginPath();
        ctx.fillStyle = "#fdd700";
        ctx.moveTo(vertices[face[0]].x, vertices[face[0]].y);
        ctx.lineTo(vertices[face[1]].x, vertices[face[1]].y);
        ctx.lineTo(vertices[face[2]].x, vertices[face[2]].y);
        ctx.lineTo(vertices[face[3]].x, vertices[face[3]].y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }
    }
  }

  rotateX(radian) {
    const cosine = Math.cos(radian);
    const sine = Math.sin(radian);

    for (let index = this.vertices.length - 1; index > -1; --index) {
      const p = this.vertices[index];

      const y = (p.y - this.y) * cosine - (p.z - this.z) * sine;
      const z = (p.y - this.y) * sine + (p.z - this.z) * cosine;

      p.y = y + this.y;
      p.z = z + this.z;
    }
  }

  rotateY(radian) {
    const cosine = Math.cos(radian);
    const sine = Math.sin(radian);

    for (let index = this.vertices.length - 1; index > -1; --index) {
      const p = this.vertices[index];

      const x = (p.z - this.z) * sine + (p.x - this.x) * cosine;
      const z = (p.z - this.z) * cosine - (p.x - this.x) * sine;

      p.x = x + this.x;
      p.z = z + this.z;
    }
  }
}
