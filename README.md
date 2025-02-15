# Llama-2-chat-finetuned 🎬🤖  

A fine-tuned **Llama-2-7b-chat** model optimized for movie-related conversations! This model understands movie genres, actors, directors, and can even recommend films based on your preferences.  

## 🚀 Features  

- **Movie Q&A:** Ask about movies, actors, directors, and genres.  
- **Movie Recommendations:** Get movie suggestions based on your interests.  
- **Conversational AI:** Engages in movie-related discussions.  

## 📌 Model Details  

- **Base Model:** [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)  
- **Fine-Tuned By:** HiTruong  
- **Fine-Tuning Method:** LoRA (Low-Rank Adaptation)  
- **Dataset:** Movie-related dataset  
- **Evaluation Metric:** BLEU Score  
- **BLEU Score Before Fine-Tuning:** 33.26  
- **BLEU Score After Fine-Tuning:** 77.53  
- **Hosted On:** [Hugging Face 🤗](https://huggingface.co/HiTruong/Llama-2-chat-finetuned)

## 🐳 Deploy with Docker  

### 1️⃣ Pull the Docker Image  

```bash
docker pull hitruong05/movie-chatbot
```

### 2️⃣ Run the Container

```
docker run -p 7860:7860 hitruong05/movie-chatbot
```
The chatbot will now be accessible on 
```
http://localhost:8501
```
---

## 📌 About
- **Author**: HiTruong
- **Built with**: Python, Docker
- **License**: MIT
- **Docker Hub**: [Docker Hub](https://hub.docker.com/repository/docker/hitruong05/movie-chatbot/general) 🐳
---

## 📞 Contact  
If you have any questions or suggestions, feel free to reach out:  
- **📧 Email**: [hitruong.work@gmail.com](mailto:hitruong.work@gmail.com)  
- **🔗 LinkedIn**: [linkedin.com/in/hitruong](https://www.linkedin.com/in/hitruong/)  
---

## ⭐ If you like this project, give it a star and share it! 🚀
