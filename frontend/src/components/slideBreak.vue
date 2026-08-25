<template>
  <Swiper
    :slides-per-view="1"
    :space-between="10"
    :autoplay="{
      delay: 2500,
      disableOnInteraction: false,
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
    <SwiperSlide
      v-for="item in data"
      :key="item.id"
    >
      <div class="card">

        <!-- Product Image -->
        <div class="image-wrapper">
          <img
            :src="item.image"
            :alt="item.product_name"
          />
        </div>

        <!-- Product Information -->
        <div class="card-content">

         <Tag
            :value="item.status"
            :severity="item.status === 'In Stock' ? 'success' : 'danger'"
          />

          <h3 class="product-name" style="margin-top:10px">
            {{ item.product_name }}
          </h3>

          <p class="price">
            ${{ item.price.toLocaleString() }}
          </p>

        </div>

      </div>
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
import Tag from 'primevue/tag'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay } from 'swiper/modules'

import 'swiper/css'

const modules = [Autoplay]

const data = [
  {
    id: 1,
    image:
      'https://imgs.search.brave.com/EPnJnNizMbCvdngfXf-PzsjK2-uCz-_JjmaOMNYmwj8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nL2NOMEFB/T1N3RUdGbEpRQUkv/cy1sOTYwLndlYnA',
    product_name: 'Apple MacBook Pro 16',
    price: 1000,
    status: 'In Stock',
  },

  {
    id: 2,
    image:
      'https://imgs.search.brave.com/wYWxTwLQ3lpfr8fLjji4S8jN9_dRH0dSEjqchgv8jkY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9waXNj/ZXMuYmJ5c3RhdGlj/LmNvbS9pbWFnZTIv/QmVzdEJ1eV9VUy9p/bWFnZXMvcHJvZHVj/dHMvNWIxODcwOGEt/ZTZmNC00YTNkLThj/MWUtMWNjOTQyYmEy/ZWIwLnBuZw',
    product_name: 'Asus ROG Strix G15s',
    price: 15500,
    status: 'Out Stock',
  },

  {
    id: 3,
    image:
      'https://imgs.search.brave.com/Vr6nxGUmCtGRFmcVf4TSUr1O89tN6KWMUDGLWO0IlzU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jb250/ZW50LmFidC5jb20v/aW1hZ2UucGhwL2Vj/NWI4Yjg5YTUyNTIz/YjdmODg2MjdlNDJm/OGIxM2Q2P2ltYWdl/PS9pbWFnZXMvcHJv/ZHVjdHMvQkRQX0lt/YWdlcy9hc3VzLXBv/cnRhYmxlLW1vbml0/b3ItTUIxNjlDSy1h/bmdsZWQuanBnJmNr/PTI',
    product_name: 'Asus ROG Strix G15d',
    price: 15500,
    status: 'Out Stock',
  },

  {
    id: 4,
    image:
      'https://imgs.search.brave.com/azghGHp8y-ONgKwIDsd5YCoMUEJ79Kx5O3YOZ0sCO0M/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE3/MTc4NjU0OTk4NTct/ZWMzNWNlNmU2NWZh/P2ZtPWpwZyZxPTYw/Jnc9MzAwMCZhdXRv/PWZvcm1hdCZmaXQ9/Y3JvcCZpeGxpYj1y/Yi00LjEuMCZpeGlk/PU0zd3hNakEzZkRC/OE1IeHpaV0Z5WTJo/OE0zeDhiV0ZqWW05/dmF5VXlNR0ZwY254/bGJud3dmSHd3Zkh4/OE1BPT0',
    product_name: 'Asus ROG Strix G15',
    price: 15500,
    status: 'Out Stock',
  },

  {
    id: 5,
    image:
      'https://imgs.search.brave.com/wYWxTwLQ3lpfr8fLjji4S8jN9_dRH0dSEjqchgv8jkY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9waXNj/ZXMuYmJ5c3RhdGlj/LmNvbS9pbWFnZTIv/QmVzdEJ1eV9VUy9p/bWFnZXMvcHJvZHVj/dHMvNWIxODcwOGEt/ZTZmNC00YTNkLThj/MWUtMWNjOTQyYmEy/ZWIwLnBuZw',
    product_name: 'Asus ROG Strix G15',
    price: 15500,
    status: 'Out Stock',
  },

  {
    id: 6,
    image:
      'https://imgs.search.brave.com/_HobGsnJpT18QX31W2cO6TXjJXU81zry5dYDImOljwg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nLzFDY0FB/T1N3TnRwa0MxUmMv/cy1sOTYwLndlYnA',
    product_name: 'Dell XPS 15',
    price: 1020,
    status: 'In Stock',
  },

  {
    id: 7,
    image:
      'https://imgs.search.brave.com/_HobGsnJpT18QX31W2cO6TXjJXU81zry5dYDImOljwg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nLzFDY0FB/T1N3TnRwa0MxUmMv/cy1sOTYwLndlYnA',
    product_name: 'Dell XPS 15',
    price: 1070,
    status: 'In Stock',
  },

  {
    id: 8,
    image:
      'https://imgs.search.brave.com/_HobGsnJpT18QX31W2cO6TXjJXU81zry5dYDImOljwg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nLzFDY0FB/T1N3TnRwa0MxUmMv/cy1sOTYwLndlYnA',
    product_name: 'Dell XPS 15',
    price: 14040,
    status: 'In Stock',
  },
  {
    id: 9,
    image:
      'https://imgs.search.brave.com/_HobGsnJpT18QX31W2cO6TXjJXU81zry5dYDImOljwg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nLzFDY0FB/T1N3TnRwa0MxUmMv/cy1sOTYwLndlYnA',
    product_name: 'Dell XPS 15ss',
    price: 14040,
    status: 'In Stock',
  },
  {
    id:10,
    image:
      'https://imgs.search.brave.com/_HobGsnJpT18QX31W2cO6TXjJXU81zry5dYDImOljwg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmVi/YXlpbWcuY29tL2lt/YWdlcy9nLzFDY0FB/T1N3TnRwa0MxUmMv/cy1sOTYwLndlYnA',
    product_name: 'Dell XPS 15dd',
    price: 14040,
    status: 'In Stock',
  },
]
</script>

<style scoped>
.mySwiper {
  width: 100%;
}

.card {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  background: white;
  border: 1px solid #e5e5e5;
  border-radius: 9px;
  overflow: hidden;
}

.image-wrapper {
  width: 100%;
  height: 180px;

  display: flex;
  align-items: center;
  justify-content: center;

  overflow: hidden;
  background: #f8f8f8;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  width: 100%;
  padding: 12px;
  box-sizing: border-box;
  text-align: left;
}

.status {
  margin: 0 0 6px;
  font-size: 13px;
  font-weight: 600;
}

.in-stock {
  color: #16a34a;
}

.out-stock {
  color: #dc2626;
}

.product-name {
  margin: 0 0 8px;
  font-size: 16px;
  font-weight: 600;
  color: #222;
}

.price {
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  color: #111;
}
</style>