import streamlit as st

st.set_page_config(
    page_title="Omoshiroki",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
    )

import time
import random
import pandas as pd
import numpy as np
import pydeck as pdk
import datetime
from PIL import Image
img = Image.open("ishin.jpg")
img2 = Image.open("shinsaku.jpg")
img3 = Image.open("plot1.JPG")
img4 = Image.open("plot2.JPG")
img5 = Image.open("noryoku.JPG")
img6 = Image.open("jyugun.JPG")
img7 = Image.open("omoshiroki.jpg")
img8 = Image.open("blog.JPG")
img9 = Image.open("Weed1.jpg")
img10 = Image.open("Weed2.jpg")
img11 = Image.open("Weed3.jpg")
st.balloons()

st.title("Omoshiroki 自己研鑽の記録")

st.write("ロード状況")
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration:{i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

st.info('All about us')
expander1 = st.beta_expander("Omoshirokiとはなんですか")
expander1.write("｢AIを駆使し、社会と自分のために働く集団｣それがOmoshirokiです。\n名前の由来は幕末の長州藩の志士　高杉晋作の辞世の句\
｢おもしろき　こともなく世を　おもしろく｣から。\n激動の時代、幕末の志士たちが日本を救うため命を賭けて学び、\n戦ったように、社会の閉塞感を自らの意志で打ち払い、\
そこに楽しさすら見いだすような生き様を見せていきたいと\n思っています。")
expander1.image(img, caption="岩倉使節団", use_column_width=True)
expander1.image(img2, caption="高杉晋作", use_column_width=True)

st.info('自己研鑽の足跡')

st.write("１．アプリケーションの開発")
expander2 = st.beta_expander("①信長様とのサシ呑み")
video_file = open('sashinomi.mp4', 'rb')
video_bytes = video_file.read()
expander2.write("最初に開発したデスクトップアプリ。上部にあるボタンをクリックするとサシ呑み中の信長が、部下の愚痴や過去の自慢話をランダムで話すという、かなり下らない内容。")
expander2.video(video_bytes)

expander3 = st.beta_expander("②新人 織田担当員の挑戦(音声注意)")
video_file = open('oda-tantouin.mp4', 'rb')
video_bytes = video_file.read()
expander3.write("トヨタ生産方式をゲーミフィケーションの手法で学習できないかという着眼で作成。ゲーム開発にそこまで向いていないPythonでフリー音源を使用して開発したため、昔懐かしいファミリーコンピューターを彷彿とさせる。")
expander3.video(video_bytes)

expander4 = st.beta_expander("③戦国武将録 with　Wikipedia")
video_file = open('busho_wiki.mp4', 'rb')
video_bytes = video_file.read()
expander4.write("後述する信長の野望大志のデータセットとWikipediaの情報をAPIを使って組み合わせられないかにトライしたもの。Wikiを読み込むため若干速度が出ないが、初めて作成できた実用性のあるアプリ。")
expander4.video(video_bytes)

st.write("２．データ分析")
expander5 = st.beta_expander("①信長の野望データセットの分析")
expander5.write("Numpyやmatplotlibなどの練習に行った分析。信長の野望の武将のパラメーターの相関を調べたり、「家名存続」しか考えていない奴は能力値が低いなど、ゲームを通じて漠然と思った仮説を検証していくのが楽しかった。ただ、一番印象に残っているのはデータセットを作るのに膨大に時間がかかったこと…。")
expander5.image(img3, use_column_width=True)
expander5.image(img5, use_column_width=True)
expander6 = st.beta_expander("②信長家の従軍状況に基づく信頼性の分析")
expander6.write("Network Xを使い、織田家が経験した全ての戦さの参戦回数と同じ戦にどれだけ一緒に参陣しているかで、織田家の人間関係を探ろうとしたもの。学校や会社などでの人間関係分析に活用できる可能性を感じた")
expander6.image(img6, use_column_width=True)

st.write("３．画像処理・検出")
expander7 = st.beta_expander("①opencvによる画像処理")
expander7.write("ゆくゆくはロボットによる自動検出をするために、Udemyの講座をベースにopencvの機能を一通り学習。所詮、動画も写真もdotの集まりなんだなあと強く実感。")
video_file = open('gradation.mp4', 'rb')
video_bytes = video_file.read()
expander7.video(video_bytes)

expander8 = st.beta_expander("②yoloV5による画像検出")
expander8.write("既存のモデルをそのまま活用した画像検出。出来てうれしかったが、これの精度を上げていく技術を身につけるという点においては、まだとてつもない高い壁があるということを実感した。")
video_file = open('kodomoheya.mp4', 'rb')
video_bytes = video_file.read()
expander8.video(video_bytes)

st.write("４．Deep Learning")
expander9 = st.beta_expander("Tensorflow keras による雑草の判別器を実装")
expander9.write("似た三種類の雑草の分類を、判別器実装してトライ。テストデータでは100％の結果でも、本番では7割前後の正解率で、過学習という言葉の意味が理解できたトライだった。")
expander9.image(img9, use_column_width=True)
expander9.image(img10, use_column_width=True)
expander9.image(img11, use_column_width=True)

st.write("５．Web開発")
expander10 = st.beta_expander("①djangoでのOmoshiroki blog デプロイ")
expander10.write("初めて自分の力でWeb上にデプロイしたもの。自分の力などといったが、djangoのチュートリアルを少し変えただけ。でも、初めてデプロイ出来たときは声が出るくらい嬉しかった。")
expander10.image(img8, use_column_width=True)
expander11  = st.beta_expander("②StreamlitによるWebサイトのデプロイ")
expander11.write("このWebのこと。できることは若干限られるかもしれないけれど、CSS,HTML,javascriptを書かなくていいのは嬉しい。")

st.sidebar.write("Contact Us")
st.sidebar.write("Omoshiroki　~死に物狂いでも心に平安~")
st.sidebar.image(img7, use_column_width=True)
st.sidebar.write("<E-mail> japanhistorydiscovery@gmail.com")


