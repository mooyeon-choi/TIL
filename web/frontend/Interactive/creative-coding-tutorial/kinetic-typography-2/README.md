# Kinetic Typography #2

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
