<template>
  <Swiper
    :slides-per-view="1"
    :space-between="10"
    :autoplay="{
      delay: 2500,
      disableOnInteraction: false,
    }"
    :pagination="{
      clickable: true,
    }"
    :breakpoints="{
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 4,
        spaceBetween: 20,
      },
      1024: {
        slidesPerView: 5,
        spaceBetween: 20,
      },
    }"
    :modules="modules"
    class="mySwiper"
  >
    <SwiperSlide v-for="item in items" :key="item.id">
      <div class="card">
        {{ item.name }}
      </div>
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Pagination, Autoplay } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/pagination';

const modules = [Pagination, Autoplay];

const items = [
  { id: 1, name: 'Slide 1' },
  { id: 2, name: 'Slide 2' },
  { id: 3, name: 'Slide 3' },
  { id: 4, name: 'Slide 4' },
  { id: 5, name: 'Slide 5' },
  { id: 6, name: 'Slide 6' },
  { id: 7, name: 'Slide 7' },
  { id: 8, name: 'Slide 8' },
  { id: 9, name: 'Slide 9' },
];
</script>

<style scoped>
.mySwiper {
  width: 100%;
  padding-bottom: 40px;
}

.card {
  width: 100%;
  height: 100%;

  display: flex;
  align-items: center;
  justify-content: center;

  background: white;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
}
</style>