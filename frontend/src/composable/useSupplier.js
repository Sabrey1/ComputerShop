import { ref } from 'vue'
import axios from '../services/axios.js'
const suppliers = ref([])

export function useSupplier(){

    async function getSupplier(){
        const res = await axios.get('supplier')
        if(res.data){
            suppliers.value = res.data
        }
    }
    return {
        getSupplier,
        suppliers
    }
}