# TensorFlow

> Open source Machine Learning Flatform
>
> TensorFlow 학습 페이지를 보고 공부한 내용을 정리하였습니다.

## 목차

* [Keras를 활용한 Neural Style Transfer](#keras를-활용한-neural-style-transfer)

## Keras를 활용한 Neural Style Transfer

* [바로가기](./neural-style-transfer)

```
Neural style transfer은 Content Image와 Style Reference Image를 이용하여
이미지의 콘텐츠는 유지하되 스타일 참조 이미지의 화풍으로 채색한 것 같은 새로운 이미지를 생성하는 최적화 기술이다.
이를 tf.keras model을 사용하여 구현하는 방법을 간단한 실습을 통해 배워보았다.
```

| Content Image                                                | Style Reference Image                                        | Result Image                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg" width="300px" /> | <img src="https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg" width="300px" /> | <img src="https://tensorflow.org/tutorials/generative/images/stylized-image.png" width="300px" /> |

