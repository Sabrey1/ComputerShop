import { ref } from 'vue'
import axios from '../services/axios.js'
const imageSlide = ref([])

export function useImageSlide(){

    async function getImageSlide(){
        const res = await axios.get('image_slide')
        if(res.data){
            imageSlide.value = res.data
        }
    }
    return {
        getImageSlide,
        imageSlide
    }
}