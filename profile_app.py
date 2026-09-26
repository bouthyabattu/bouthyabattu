import streamlit as st

st.set_page_config(page_title="Bouthya Battu | Data Analyst", page_icon="👋", layout="wide")

st.markdown("""
<style>
.block-container{max-width:1200px;padding-top:2rem}
.center{text-align:center}.subtitle{text-align:center;color:#00BFFF}
.card{padding:1.25rem;border:1px solid #30363d;border-radius:12px;background:#161b22;height:100%}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='center'>Hi 👋, I'm Bouthya Battu</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Aspiring Data Analyst • ML Enthusiast • DSA Learner</h3>", unsafe_allow_html=True)

st.image("https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=22&duration=3000&pause=700&color=00BFFF&center=true&vCenter=true&width=700&lines=Turning+Data+Into+Insights;Data+Analytics+%7C+Business+Intelligence;Python+%7C+Java+%7C+Machine+Learning;Power+BI+%7C+SQL+%7C+Data+Visualization;Learning+DSA+%26+Advanced+Machine+Learning", width=700)
st.image("https://komarev.com/ghpvc/?username=bouthyabattu&label=Profile%20Views&color=00F5D4&style=flat-square", width=150)
st.divider()

about, coding = st.columns([1.35,1])
with about:
    st.header("👨‍💻 About Me")
    st.markdown("""
- 🔭 Currently working on **Data Science and Business Analytics**
- 🌱 Currently learning **Advanced Data Science and Machine Learning**
- 📊 Interested in **Data Analytics, Business Intelligence & ML**
- 💬 Ask me about **Python, Data Science, Business Intelligence & SQL**
- 📫 Reach me at **bouthyabattu07@gmail.com**
- ⚡ Fun fact: **I love turning data into stories**
- 🎯 Goal: **Build data-driven solutions that create real-world impact**
""")
with coding:
    st.image("https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif", caption="Coding")

st.divider()
st.header("🌐 Connect With Me")
cols=st.columns(5)
for col,label,url in zip(cols,["LinkedIn","Instagram","GitHub","Email","X"],["https://www.linkedin.com/in/bouthya-battu/","https://instagram.com/bouthya_battu/","https://github.com/bouthyabattu","mailto:bouthyabattu07@gmail.com","https://x.com/bouthya"]):
    col.link_button(label,url)

st.divider()
st.header("🛠️ Tech Stack")
stacks={
"💻 Programming Languages":"c,java,javascript,python,r,scala",
"📊 Data Science & Machine Learning":"anaconda,pytorch,tensorflow",
"🌐 Web Development":"css,flask,flutter,nodejs,react,tailwind",
"🗄️ Databases & Cloud":"firebase,mongodb,mysql,postgresql,aws,googlecloud",
"⚙️ Tools & DevOps":"docker,git,github,kafka,vercel,vscode"}
for title,icons in stacks.items():
    st.subheader(title)
    st.image(f"https://skillicons.dev/icons?i={icons}",width=650)

st.divider()
for title,url in [
("📊 GitHub Statistics","https://github-readme-stats.shion.dev/api?username=bouthyabattu&theme=dark&hide_border=false&include_all_commits=true&count_private=true"),
("🔥 GitHub Streak","https://streak-stats.demolab.com/?user=bouthyabattu&theme=dark&hide_border=false"),
("🔥 Most Used Languages","https://github-readme-stats.shion.dev/api/top-langs/?username=bouthyabattu&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact&cache_count=1800")]:
    st.header(title); st.image(url,width=850)

st.divider()
st.header("📈 Contribution Activity")
st.image("https://raw.githubusercontent.com/bouthyabattu/bouthyabattu/main/assets/contribution-graph.svg",use_container_width=True)
st.divider()
st.header("🐍 Contribution Snake")
st.image("https://raw.githubusercontent.com/bouthyabattu/bouthyabattu/output/github-contribution-grid-snake-dark.svg",use_container_width=True)
st.divider()
st.header("🏆 GitHub Trophies")
st.image("https://github-profile-trophy.vercel.app/?username=bouthyabattu&theme=tokyonight&no-frame=true&no-bg=true&margin-w=5&row=1",use_container_width=True)

st.divider()
st.header("🚀 Featured Projects")
p1,p2=st.columns(2)
with p1:
    st.markdown("<div class='card'><h3>🧠 Sentiment Analysis on Social Media</h3><p>Machine Learning and NLP project that analyzes public opinions and extracts meaningful sentiment patterns from social media data.</p><strong>Tech:</strong> Python • NLP • Machine Learning • Pandas</div>",unsafe_allow_html=True)
with p2:
    st.markdown("<div class='card'><h3>📊 Diwali Sales Data Analysis</h3><p>Exploratory Data Analysis project focused on identifying customer behavior, purchasing patterns and festive sales trends.</p><strong>Tech:</strong> Python • Pandas • NumPy • Matplotlib • Seaborn</div>",unsafe_allow_html=True)

st.divider()
st.header("🎯 Current Learning Journey")
st.code("""Data Analytics
      │
      ├── Python
      ├── SQL
      ├── Excel
      └── Power BI
             │
             ▼
      Data Visualization
             │
             ▼
      Machine Learning
             │
             ├── Supervised Learning
             ├── Unsupervised Learning
             ├── NLP
             └── Model Evaluation
                    │
                    ▼
              Advanced ML
                    │
                    ▼
              Real-World AI""")
