import { ref } from 'vue'
import axios from '../services/axios.js'
const customers = ref([])

export function useCustomer(){

    async function getCustomer(){
        const res = await axios.get('customer')
        if(res.data){
            customers.value = res.data
        }
    }
    return {
        getCustomer,
        customers
    }
}