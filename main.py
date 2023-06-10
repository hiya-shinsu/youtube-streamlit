import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')
st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右に文字を表示')

expaner = st.expander('問い合わせ')
expaner.write('問い合わせ内容')

if button:
    right_column.write('ここは右カラムです')


condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition, 'です。' 

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text, 'です。'

'あなたの好きな数字は、', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('test.png')
    st.image(img, caption='test', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4 ],
    '2列目': [10, 20, 30, 40 ]
})

graph = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(graph)

st.area_chart(graph)
st.bar_chart(graph)

st.table(df.style.highlight_max(axis=0))
st.write(df.style.highlight_max(axis=0))
st.dataframe(df, width=100, height=100)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
