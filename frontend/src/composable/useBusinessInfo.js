import { ref } from 'vue'

import axios from '../services/axios.js'

const businessInfo = ref([])
export function useBusinessInfo(){
    
    async function getBusinessInfo(){
        const res = await axios.get('business_info')
        if(res.data){
            businessInfo.value = res.data
        }
    }

    return {
        getBusinessInfo,
        businessInfo
    }
}