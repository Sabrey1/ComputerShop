import { ref } from 'vue'
import axios from '../services/axios.js'
const categories = ref([])

export function useCategory(){

    async function getCategory(){
        const res = await axios.get('categories')
        if(res.data){
            categories.value = res.data
        }
    }
    return {
        getCategory,
        categories
    }
}