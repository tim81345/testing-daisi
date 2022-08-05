import os
import streamlit as st
import skimage

def get_image():
    '''
    fetch an ai generated face image

    :return: numpy array that is the image
    '''
    os.system('curl https://thispersondoesnotexist.com/image > image.jpg')
    image_numpy = skimage.io.imread('image.jpg')
    return image_numpy

if __name__ == '__main__':
    st.title("AI generated faces")
    st.write("This is a demo of ai generated faces (stylegan2)")
    with st.sidebar:
        go_button = st.button("Generate")
    
    if go_button:
        result = get_image()
        st.image(result, width=512)