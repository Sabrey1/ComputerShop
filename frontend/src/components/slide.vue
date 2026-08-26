<template>
  <swiper
    :spaceBetween="30"
    :centeredSlides="true"
    :autoplay="{
      delay: 2500,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    class="mySwiper"
  >
    <swiper-slide
      v-for="item in [...imageSlide]
      .filter(item=>item.enable)
      .sort((a,b ) => a.sort_order - b.sort_order)"
      :key="item.id"
    >
      <img
        :src="item.image"
        :alt="item.title"
      />
    </swiper-slide>
  </swiper>
</template>
<script>
  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  import 'swiper/css/pagination';
  import 'swiper/css/navigation';

  import '../style.css';

  import { ref, onMounted } from 'vue'

import { useImageSlide } from "../composable/useImageSlide.js"


  // import required modules
  import { Autoplay, Pagination, Navigation } from 'swiper/modules';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      const { getImageSlide,
        imageSlide } = useImageSlide()
      onMounted(() => {
        getImageSlide()
      });
      return {
        modules: [Autoplay, Pagination, Navigation],imageSlide,
      };
    },
  };
</script>
