import streamlit as st 
import google.generativeai as genai
from apikey import *
import pickle 


st.set_page_config(layout="wide",page_title="AI Blog Companion")

  

genai.configure(api_key=google_gemini_api_key)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
  }

safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  # Setting our model 
model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",generation_config=generation_config,safety_settings=safety_settings)



st.title("BlogCraft: Your AI Writing Companion")

st.subheader("Now you can craft perfect blogs with the help of AI- BlogCraft is your New AI Blog Companion")


with st.sidebar:
      

  st.title("Input Your Blog Details")
  st.subheader("Enter Details of the Blog You want to generate")

      # Blog title 
  blog_title=st.text_input("Blog Title")

      # Keywords input
  keywords=st.text_area("Keywords (comma-seperated)")

      # Number of words
  num_words=st.slider("Number of words",min_value=250,max_value=2000,step=1000)

      # Number of images 
  num_images=st.number_input("Number of images",min_value=1,max_value=5,step=1)

  prompt_parts=[f"“Generate a comprehensive, engaging blog post relevant to the given title {blog_title} and keywords{keywords}. Make sure to incorporate these keywords in blog post.The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.”"]
      # Submit button
  submit_button=st.button("Generate Blog")

convo = model.start_chat(history=[
    {
      "role": "user",
      "parts": [f"“Generate a comprehensive, engaging blog post relevant to the given title {blog_title} and keywords{keywords}. Make sure to incorporate these keywords in blog post.The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.”"]
    },
    {
      "role": "model",
      "parts": ["## The Ripple Effect: Exploring the Impact of Generative AI\n\nGenerative AI, the technology capable of producing entirely new content like text, images, and even music, is making waves across industries. This innovative branch of artificial intelligence holds immense potential, promising a revolution in creative fields and beyond. But with great power comes great responsibility, and the ethical implications of this technology are just beginning to be explored.\n\nOne of the most significant effects of generative AI is its impact on **artificial creativity**. By analyzing vast datasets of existing works, these algorithms can generate original content that mimics human creativity. This has led to exciting applications like AI-powered music composition, text generation for marketing materials, and even the creation of realistic artwork. While this opens doors for new forms of expression and artistic exploration, it also raises questions about the nature of creativity itself. Can machines truly be creative, or are they simply mimicking the patterns they have learned?\n\nThe ethical implications of generative AI extend far beyond the realm of art. The ability to create hyper-realistic fake content, known as deepfakes, presents a major challenge in combating misinformation and manipulation. Imagine realistic videos of political figures saying things they never did, or fabricated news articles designed to sway public opinion. This technology has the potential to erode trust in media and institutions, and safeguarding against its misuse is crucial.\n\nDespite these concerns, generative AI also offers a wealth of positive possibilities. Its applications in **machine learning** are driving innovation across various sectors. In healthcare, it can be used to generate synthetic medical data for research and training, potentially leading to faster diagnoses and more effective treatments. In education, AI-powered tutors can personalize learning experiences and provide tailored feedback to students. The potential for positive **AI impact on society** is vast, and harnessing its power responsibly is key.\n\nAs with any transformative technology, navigating the ethical landscape of generative AI requires careful consideration. Open dialogue and collaboration between developers, policymakers, and the public are crucial to ensure its responsible development and deployment. We must address concerns around bias, ensure transparency in how these algorithms operate, and prioritize the protection of individual privacy.\n\nGenerative AI is still in its infancy, but its potential to reshape our world is undeniable. By approaching this technology with caution and a commitment to ethical principles, we can harness its power to foster innovation, enhance creativity, and ultimately create a better future for all."]
    },
    {
      "role": "user",
      "parts": [f"User“Generate a comprehensive, engaging blog post relevant to the given title {blog_title} and keywords {keywords}. Make sure to incorporate these keywords in blog post.The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.”"]
    },
    {
      "role": "model",
      "parts": ["## The Ripple Effect: Exploring the Impact of Generative AI\n\nGenerative AI, a cutting-edge branch of artificial intelligence, is making waves across industries, promising to revolutionize creative fields and beyond. By analyzing vast datasets and learning from existing works, these algorithms can generate entirely new and original content, ranging from text and images to music and even videos.\n\n**Artificial Creativity and Ethical Implications**\n\nOne of the most significant effects of generative AI is its impact on artificial creativity. These algorithms can mimic human creativity, generating content that is often indistinguishable from human-created works. This has led to exciting applications like AI-powered music composition, text generation for marketing materials, and the creation of realistic artwork.\n\nHowever, the ethical implications of generative AI cannot be ignored. The ability to create hyper-realistic fake content, known as deepfakes, presents a major challenge in combating misinformation and manipulation. Imagine realistic videos of political figures saying things they never did, or fabricated news articles designed to sway public opinion. This technology has the potential to erode trust in media and institutions, and safeguarding against its misuse is crucial.\n\n**Technology Innovation and Machine Learning Applications**\n\nDespite these concerns, generative AI also offers a wealth of positive possibilities. Its applications in machine learning are driving innovation across various sectors. In healthcare, it can be used to generate synthetic medical data for research and training, potentially leading to faster diagnoses and more effective treatments. In education, AI-powered tutors can personalize learning experiences and provide tailored feedback to students.\n\n**AI Impact on Society**\n\nThe potential for positive AI impact on society is vast. Generative AI can be used to create personalized educational content, enhance accessibility to information for people with disabilities, and even develop new therapies for mental health conditions. By harnessing its power responsibly, we can create a more equitable and inclusive society for all.\n\n**Navigating the Ethical Landscape**\n\nAs with any transformative technology, navigating the ethical landscape of generative AI requires careful consideration. Open dialogue and collaboration between developers, policymakers, and the public are crucial to ensure its responsible development and deployment. We must address concerns around bias, ensure transparency in how these algorithms operate, and prioritize the protection of individual privacy.\n\n**Conclusion**\n\nGenerative AI is still in its infancy, but its potential to reshape our world is undeniable. By approaching this technology with caution and a commitment to ethical principles, we can harness its power to foster innovation, enhance creativity, and ultimately create a better future for all."]
    },
  ])

convo.send_message("YOUR_USER_INPUT")

if submit_button:

      
      st.write(convo.last.text)
    





