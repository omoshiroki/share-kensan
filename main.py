import streamlit as st
import time
img = Image.open("ishin.jpg")
img2 = Image.open("shinsaku.jpg")



st.title("自己研鑽共有アプリ Share-Kensan\n～Rivals still growing～")

"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration:{i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)


option2 = st.sidebar.text_input("あなたの自己研鑽したいことを教えてください")
condition = st.sidebar.slider("あなたの自己研鑽へのモチベーションは？",0,100,10)

"あなたの自己研鑽：",option2
"モチベーション：", condition

st.write("<このアプリケーションについて>")
st.write("明治維新。諸外国の圧力により人々の心が揺れる中、国の行く末を案じ、奔走し続けた志士たちがいました。\
    現在の日本の状況もまさに維新。自らを変え、周りをも変えていかねば、個人としても国としても生き残ることはありません。\
    自らを変えるには、同じ目標に向かい、ともに努力するよき友・よきライバルが必要です。このアプリケーションが\
    よい意味で全員の対抗意識を燃やし、自己変革していく一助となればと思います。")

left_column, right_column = st.beta_columns(2)

left_column, right_column = st.beta_columns(2)
left_column.image(img, caption="岩倉使節団", use_column_width=True)
right_column.image(img2, caption="高杉晋作", use_column_width=True)
#st.image(img, caption="岩倉使節団", use_column_width=True)

#st.image(img2, caption="高杉晋作", use_column_width=True)
#option  = st.selectbox(
#    "あなたが好きな数字を教えてください。",
#    list(range(1, 11))
#)

#"あなたの好きな数字は", option, "です。"


button = left_column.button("運営団体名を知りたい方はPush")
if button:
    right_column.write("Omoshiroki")

st.write("<お問い合わせ>")
expander1 = st.beta_expander("Omoshirokiとはなんですか")
expander1.write("Omoshirokiは、AIを駆使し、社会のため、そして自分のために働く集団です。")

expander1 = st.beta_expander("Omoshirokiに加入することはできますか？")
expander1.write("社会を、そして日本を変える志のある方は常にWelcomeです。")



