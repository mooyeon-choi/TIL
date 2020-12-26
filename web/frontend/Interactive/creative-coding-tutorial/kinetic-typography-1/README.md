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
