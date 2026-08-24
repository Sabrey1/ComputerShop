import { ref } from 'vue'
import axios from '../services/axios.js'
const products = ref([])

export function useProduct(){

    async function getProduct(){
        const res = await axios.get('product')
        if(res.data){
            products.value = res.data
        }
    }
    return {
        getProduct,
        products
    }
}