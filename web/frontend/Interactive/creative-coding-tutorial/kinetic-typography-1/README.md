# Kinetic Typography #1

## MENU

* [Get Started](#get-started)

## Get Started

### Web Font Loader

* [Github](https://github.com/typekit/webfontloader)

* `index.html` 추가

  ```html
  <head>
      ...
      ...
      <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js"></script>
  </head>
  ```

* `app.js` 추가

  ```js
  WebFont.load({
        google: {
          families: ["Hind:700"],
        }
      });
  ```

### PixiJS

* [Github](https://github.com/pixijs/pixi.js)

* CDN install (`index.html` 추가)

  ```html
  <head>
  	<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/5.1.3/pixi.min.js"></script>    
  </head>
  ```
  
* `PIXI.Renderer()`

  * [공식문서](https://pixijs.download/release/docs/PIXI.Renderer.html)
  * WebGL을 통해 canvas에 그려준다.

* `PIXI.Filter()`

  * [공식문서](https://pixijs.download/release/docs/PIXI.Filter.html)

  ```js
  const filter = new PIXI.Filter(vertexSrc, fragmentSrc, uniforms);
  ```

  `fragmentSrc`는 다음과 같이 `string`으로 입력한다.

  ```js
  const fragment = `
  varying vec2 vTextureCoord;
  uniform sampler2D uSampler;
  void main(void)
  {
     gl_FragColor = texture2D(uSampler, vTextureCoord);
  }
  `;
  
  const myFilter = new PIXI.Filter(null, fragment);
  ```

  
