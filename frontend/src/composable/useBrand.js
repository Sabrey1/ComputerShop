import { ref } from 'vue'
import axios from '../services/axios.js'
const brands = ref([])

export function useBrand(){

    async function getBrand(){
        const res = await axios.get('brand')
        if(res.data){
            brands.value = res.data
        }
    }
    return {
        getBrand,
        brands
    }
}