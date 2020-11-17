import * as THREE from "https://threejsfundamentals.org/threejs/resources/threejs/r122/build/three.module.js";

class App {
  constructor() {
    this.canvas = document.createElement("canvas");
    document.body.appendChild(this.canvas);
    this.ctx = this.canvas.getContext("2d");

    this.pixelRatio = window.divicePixelRatio > 1 ? 2 : 1;

    this.renderer = new THREE.WebGLRenderer(this.canvas);

    this.fov = 75;
    this.aspect = 2;
    this.near = 0.1;
    this.far = 5;
    this.camera = new THREE.PerspectiveCamera(
      this.fov,
      this.aspect,
      this.near,
      this.far
    );
    this.camera.position.z = 2;

    this.scene = new THREE.Scene();

    this.boxWidth = 1;
    this.boxHeight = 1;
    this.boxDepth = 1;
    this.geometry = new THREE.BoxGeometry(
      this.boxWidth,
      this.boxHeight,
      this.boxDepth
    );
    this.cubes = [];
    this.texture = new THREE.CanvasTexture(this.ctx.canvas);

    this.meterial = new THREE.MeshBasicMaterial({ map: this.texture });
    this.cube = new THREE.Mesh(this.geometry, this.meterial);

    this.scene.add(this.cube);
    this.cubes.push(this.cube);

    window.addEventListener("resize", this.resize.bind(this), false);
    this.resize();

    window.requestAnimationFrame(this.animate.bind(this));
  }

  resize() {
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.canvas.width = this.stageWidth * this.pixelRatio;
    this.canvas.height = this.stageHeight * this.pixelRatio;
    this.ctx.scale(this.pixelRatio, this.pixelRatio);

    this.renderer.setSize(this.stageWidth, this.stageHeight, false);
    this.camera.aspect = this.stageWidth / this.stageHeight;
    this.camera.updateProjectionMatrix();
  }

  animate(time) {
    time *= 0.001;
    window.requestAnimationFrame(this.animate.bind(this));

    this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

    this.cubes.forEach((cube, ndx) => {
      const speed = 0.2 + ndx * 0.1;
      const rot = time * speed;
      cube.rotation.x = rot;
      cube.rotation.y = rot;
    });

    this.renderer.render(this.scene, this.camera);
  }
}

window.onload = () => {
  new App();
};
