<template>
  <div class="home">

<!--Carousel-->
     <v-carousel height="600px" v-model="model" :continuous="true" :cycle="true" :show-arrows="false" hide-delimiter-background delimiter-icon="mdi-minus">
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
      >
        <v-sheet class="transparent">
          <v-col
            class=" justify-center"
            align="center">
            <div class="my-12 py-12" :class="[$vuetify.breakpoint.mdAndUp ? 'display-3' : 'display-1']">
              {{item.headline}}
            </div>
          </v-col>
        </v-sheet>
      </v-carousel-item>
      
        <v-overlay :absolute="true" :z-index="0" opacity="0" class="mt-10">
          <v-container>
            <v-layout row class="d-flex align-content-end pt-10 ">
              <v-col class="ma-0 px-1" cols="12" sm="4">
                <v-form>
                  <v-text-field class="rounded-sm" placeholder="City or adress" solo light v-model="title" :elevation="0"></v-text-field>
                </v-form>
              </v-col>

              <v-col id="selector" class="d-flex px-1 elevation-0" cols="12" sm="4">
                <v-select
                  class="rounded-sm elevation-0"
                  :items="levelName"
                  label="All levels"
                  light
                  solo
                ></v-select>
              </v-col>

              <v-col class="d-flex px-1" cols="12" sm="4">
               <v-btn block id="find" large color="warning" :elevation="0" class="rounded-sm pt-1" htight="48px">Find Player</v-btn>
              </v-col>
              
            </v-layout>
          </v-container>
        </v-overlay>
  </v-carousel>

<!--Block with button-->
  <v-container class="d-flex align-center mb-6" style="height: 400px;" >
    <v-row no-gutters  justify="center" align="center">
      <template>
        <v-col>
          <h1 class="display-3 text-center font-weight-bold"><span class="orange--text">32.110</span> Tennis players</h1>
        </v-col>
        <v-responsive width="100%"></v-responsive>
      </template>

      <template>
        <v-col>
          <p class="text-center mt-5 font-weight-thin">search by level, city and hour availability</p>
        </v-col>
        <v-responsive width="100%"></v-responsive>
      </template>

      <div class="d-flex justify-center mb-6">
      <div class="pa-2">
        <v-btn color="warning" large>Show other tennis players</v-btn>
      </div>
    </div>
    </v-row>
  </v-container>

<!--Block with background image-->
<v-img :src="require('@/frase.jpg')" style="height:400px">
    <v-container class="d-flex align-center mb-6" style="height:400px">
      <v-row no-gutters  justify="center" align="center">
        <template>
          <v-col>
            <h1 class="text-center white--text font-italic font-weight-thin" :class="[$vuetify.breakpoint.mdAndUp ? 'display-2' : 'display-1']">Improve your game, <strong class="font-weight-black">find out your statistics</strong> and <strong class="font-weight-black">simulate matches</strong> before playing the actual match</h1>
          </v-col>
          <v-responsive width="100%"></v-responsive>
        </template>
        <div class="d-flex justify-center mb-6">
      </div>
      </v-row>
    </v-container>
  </v-img>


<!--Block with parallax background image - 3 cols-->
  <v-parallax :src="require('@/slidenumeri.jpg')" style="height: 350px;">
   <v-container class="mb-6">
    <v-row no-gutters>
      <v-col
        v-for="item in info"
        :key="item.val"
        cols="12"
        sm="4"
        class="pa-2 px-7"
      >
        <div class="pa-2 px-7">
          <h1 class="display-4 font-weight-bold text-center" :class="[$vuetify.breakpoint.mdAndUp ? 'display-4' : 'display-1']">{{item.val}}</h1>
          <p class="text-center text-uppercase font-weight-medium">{{item.category}}</p>
        </div>
      </v-col>
    </v-row>
  </v-container>
</v-parallax>
 
 <!--Block with button-->
  <v-container class="d-flex align-center mb-6" style="height: 400px;" >
    <v-row no-gutters  justify="center" align="center">
      <template>
        <v-col>
          <h1 class="display-3 text-center font-weight-bold">Amateur tennis matches</h1>
        </v-col>
        <v-responsive width="100%"></v-responsive>
      </template>

      <template>
        <v-col>
          <p class="text-center mt-5 font-weight-thin">In our regional and itinerant tournaments you play at least 3 matches where and when you want</p>
        </v-col>
        <v-responsive width="100%"></v-responsive>
      </template>

      <div class="d-flex justify-center mb-6">
      <div class="pa-2">
        <v-btn color="warning" large>Show other tournaments</v-btn>
      </div>
    </div>
    </v-row>
  </v-container>
  
  <!--Block with parallax background image and buttons-->
  <v-parallax :src="require('@/bg-cta.jpg')" id="my-lax" style="height: 700px;">
    <v-container class="d-flex justify-start  mb-6">
      <v-row no-gutters  justify="start" align="center">
        <template>
          <v-col>
            <h1 class="display-3 font-weight-medium">No excuses,</h1>
            <h1 class="display-3 font-weight-medium">time to play</h1>
          </v-col>
          <v-responsive width="100%"></v-responsive>
        </template>
        <div class="d-flex justify-start mb-6">
         
        </div>
      </v-row>
    </v-container>
  </v-parallax>

  <!--Prefooter-->
   <v-container fluid class="d-flex align-center pb-6" style="height: 200px;" amber >
      <v-row no-gutters  justify="center" align="center">
        <template>
          <v-col>
            <h1 class="display-2 text-center font-weight-medium">We <v-icon  color="red darken-2" x-large>mdi-heart</v-icon> new players!</h1>
          </v-col>
          <v-responsive width="100%"></v-responsive>
        </template>
      </v-row>
    </v-container>

    <!--Footer-->
    <template>
    <v-footer
      light
      padless
    >
      <v-card
        flat
        tile
        class="grey lighten-4 text-center"
      >
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4"
            icon
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text>
          Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="black--text">
          {{ new Date().getFullYear() }} — <strong>{{this.$store.state.companyName}}</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </template>
  



  </div>
</template>

<script>

 export default {
    data: () => ({
      title: '',
      model: 0,
      colors: [
        'primary',
        'secondary',
        'yellow darken-2',
        'red',
        'orange',
      ],
      items: [
          {
            src: require('../assets/carousel/c-1.jpg'),
            headline:'We play tennis for fun!'
          },
          {
            src: require('../assets/carousel/c-2.jpg'),
            headline:'Plan matches and join tournaments'
          },
          {
            src: require('../assets/carousel/c-3.jpg'),
            headline:'No ranking, just tennis and new friends'
          },
      ],
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
    computed:{
      levels(){
        return this.$store.state.levels
      },
      levelName(){
        return this.$store.state.levels.map((lvl)=>{
          return lvl.name;
        })
      },
      info(){
        return this.$store.state.info
      }
    }
  }
</script>

<style>
  
  .v-text-field.v-text-field--solo:not(.v-text-field--solo-flat) > .v-input__control > .v-input__slot{
    box-shadow: none !important;
  }

  #find{
    height:48px;
  }

  #my-lax .v-parallax__content {
    background: linear-gradient(15deg, black, transparent);
  }
</style>>