# Project information

The project is to create a hand gesture classification model

---

- The project was made based on this [video](https://youtu.be/MJCSjXepaAM?si=5GE1ijtTPSL2BsS4)
- The project opens a window with a person’s webcam and recognize the signs that the person is showing
- The project also have a chatbot in the Telegram to interact with neural
  network [@hand_signs_recognition_bot](https://t.me/hand_signs_recognition_bot)
- Highlights: American gang signs and my favorite sign 🤟🏿
- The dataset also have the following variations of signs: *vertically mirrored, horizontally mirrored,
  vertically&horizontally mirrored*
- More details
  in [project notion](https://yesspeace.notion.site/Simple-sign-language-recognition-project-bae7d7d7f5a04b5dbc916ca165383a7d?pvs=4)
  but in Russian language

[![GIF Showing most of the signs](https://i.imgur.com/EJMMXM6.png)](https://i.imgur.com/ivDfNgl.gif)

- The dataset contains signs such as:
    - Like 👍🏿
    - Like front
    - Dislike 👎🏿
    - Dislike front
    - Ok 👌🏿
    - Peace ✌🏿
    - Rock 🤘🏿
    - YessPeace sign 🤟🏿
    - Shaka 🤙🏿
    - Fuck you 🖕🏿
    - Spock 🖖🏿
    - [West Coast](https://i.pinimg.com/1200x/5f/de/2b/5fde2bdfbe7d84925c2f71159c22b982.jpg)
    - [East Coast](https://thesource.com/wp-content/uploads/2017/10/Snoop-Dogg-Hints-New-Album-Make-America-Crip-Again.jpg)
    - [Crips](https://video-images.vice.com/videos/58dc3000466f70ae1467bb8d/lede/1510849962065-gang_initiation_approved_v2-clean.jpeg)

# Telegram Bot

- The bot can be found under the nickname [@hand_signs_recognition_bot](https://t.me/hand_signs_recognition_bot)
- The bot recognizes gestures only from photos
- The bot responds as follows

| Условия появления сообщения                                 | Сообщение                                                                                                                                                                                                                          |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The bot has a welcome message /start                        | Привет, я бот, который распознает жесты руки с картинки. Просто вышли мне фотокарточку с жестом руки.                                                                                                                              |
| Clicked the /help button                                    | Это бот для взаимодействия с нейросетею, которая расспознаёт жесты рук. Бот реагирует только на картинки и распознаёт на них знаки. Просто вышлите ему картинку, и в ответном сообщении бот выдаст картинку с распознанным знаком. |
| Clicked the /info button                                    | Это бот для взаимодействия с нейросетею, которая расспознаёт жесты рук. Данную нейросеть разработал я, Эрназаров Дамир. Подробнее о мой деятельности на [сайте](https://damir-ernazarov-yesspeace.carrd.co/)                       |
| The bot accepts the picture and displays it, but with a recognized sign. | ”Photo with recognized sign”                                                                                                                                                                                                       |
| Image weighing more than 512KB | Сорри, но ваше изображение слишком большое. Максимальный объем - 512 КБ. |
| If you send any other media file other than a photo   | Нет-нет-нет, я могу распознать жест только с фото, сорри.                                                                                                                                                                          |
| If you send a text                                    | Сорри, текст не понимаю, только команды                                                                                                                                                                                            |

[![See the video demo](https://i.imgur.com/eIOWKBh.png)](https://i.imgur.com/spIC1ag.mp4)
