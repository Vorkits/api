<template>
  <div class="tournaments">
    <!--Block with background image-->
    <v-img :src="require('@/frase.jpg')" style="height:100%">
      <v-container class="mb-10 mt-6" style="height:100%">
        <v-row no-gutters justify="center" align="center">
          <template>
            <v-col cols="12" md="10" offset-md="1">
              <v-row no-gutters>
                <v-column no-gutters style="width: 100%; padding: 5% 10% 4% 10%">
                <v-col>
                  <v-card flat class="pa-7 grey lighten-4" style="height: 100%">
                    <div class="text-center">
                      <h2 class="mb-2">LOGIN</h2>
                      <p class="text-caption mb-7">
                        Login with username and password
                      </p>
                    </div>
                    <v-form v-model="validAuth" ref="formAuth">
                      <v-row>
                        <v-col cols="12" md="12">
                          <v-text-field v-model="form.email" hide-details
                                        autocomplete="off" type="email" placeholder="E-mail"
                                        :rules="rules.email" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field v-model="form.password" hide-details
                                        placeholder="Password" min="8" type="password"
                                        :rules="rules.password" autocomplete="off" required>
                          </v-text-field>
                        </v-col>
                      </v-row>
                      <v-btn @click.prevent="login" block class="red darken-1 mt-6" dark>Enter</v-btn>
                      <!-- <a href="#" class="mt-3 d-block text-center">
                        <span class="text-caption">Forgot password</span>
                      </a> -->
                    </v-form>
                  </v-card>
                </v-col>
                <v-col>
                  <v-card flat class="pa-7 grey lighten-4" tile style="height: 100%;">
                    <div class="text-center">
                      <h2 class="mb-2">CREATE COURT</h2>
                    </div>
                    <v-form>
                      <v-row>
                        <v-col cols="12" md="12">
                          <v-text-field hide-details :rules="rules.CourtName"  v-model="form.courtName"
                                        autocomplete="off" type="text" placeholder="Court Name"
                                        required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field hide-details :rules="rules.CourtCity"  v-model="form.courtCity"
                                        autocomplete="off" type="text" placeholder="Court City"
                                        required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field hide-details :rules="rules.CourtAdress"  v-model="form.courtAdress"
                                        autocomplete="off" type="text" placeholder="Court Adress"
                                        required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field hide-details :rules="rules.CourtPhone"  v-model="form.courtPhone"
                                        autocomplete="off" type="text" placeholder="Court Phone"
                                        required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="12" style = "width: 100%; text-align: center; cursor: pointer; font-size: 1.2em;">
                          <label for="imageCourt" style = "color: black; cursor: pointer;">{{form.fileName}}</label>
                          <input :rules="rules.photo" type="file" style="display: none" @change="changePh" class = "imgCourt" id = "imageCourt" ref = "text1" required multiple accept="image/*">
                        </v-col>
                      </v-row>
                      <v-btn @click.prevent="createCourt" block class="red darken-1 mt-6" dark>Create</v-btn>
                      <!-- <a href="#" class="mt-3 d-block text-center">
                        <span class="text-caption">Forgot password</span>
                      </a> -->
                    </v-form>
                  </v-card>
                </v-col>
              </v-column>
                <v-col>
                  <v-card flat class="pa-10" tile style="height: 100%;">
                    <div class="text-center">
                      <h2 class="mb-2">REGISTER</h2>

                      <p class="text-caption mb-7">Login with e-mail</p>
                    </div>
                    <v-form v-model="validReg" ref="formReg">
                      <v-row>
                        <v-col cols="12">
                          <v-text-field v-model="form.firstName" :rules="rules.name" hide-details
                                        autocomplete="off"
                                        type="text" placeholder="First name" required>
                          </v-text-field>
                        </v-col>
                        <v-col cols="12">
                          <v-text-field v-model="form.lastName" :rules="rules.name" hide-details
                                        autocomplete="off"
                                        type="text" placeholder="Last name" required>
                          </v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field v-model="form.city" :rules="rules.city" hide-details autocomplete="off"
                                        type="text" placeholder="City" required>
                          </v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field v-model="form.email" :rules="rules.email" hide-details
                                        autocomplete="off"
                                        type="email" placeholder="email" required>
                          </v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-text-field v-model="form.password" :rules="rules.password" hide-details
                                       autocomplete="off"
                                        type="password" placeholder="password" required>
                          </v-text-field>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-checkbox :rules="rules.check" hide-details label="Stay updated" class="mt-0">
                          </v-checkbox>
                        </v-col>
                        <v-col cols="12" md="12">
                          <v-checkbox :rules="rules.check" hide-details label="I read and acceoted the terms of use" class="mt-0">
                          </v-checkbox>
                        </v-col>

                      </v-row>

                      <v-btn @click.prevent="register" block class="red darken-1 mt-6" dark>Sign up for free</v-btn>

                    </v-form>

                  </v-card>
                </v-col>
              </v-row>
            </v-col>
            <v-responsive width="100%"></v-responsive>
          </template>
          <div class="d-flex justify-center mb-6">
          </div>
        </v-row>
        <v-row no-gutters class="mt-10">
          <v-col v-for="item in info" :key="item.val" cols="12" sm="4" class="pa-2 px-2">
            <h1 class="display-3  font-weight-bold text-center" style="color: #fff"
                :class="[$vuetify.breakpoint.mdAndUp ? 'display-4' : 'display-1']">{{ item.val }}</h1>
            <div class="text-center d-block mt-3">
              <v-chip label x-large black class="d-inline mt-2" dark>
                {{ item.category }}
              </v-chip>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-img>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  data() {
    return {
      validAuth: false,
      validReg: false,
      image: null,
      form: {
        firstName: '',
        lastName: '',
        city: '',
        email: '',
        password: '',
        fileName: 'Choose Court Photo',
        courtName: '',
        courtCity: '',
        courtAdress: '',
        courtPhone: ''
      },
      rules: {
        name: [
          (v) => !!v || 'Name is required',
          v => (v || '').length > 2 || `min 3 `
        ],
        city: [
          (v) => !!v || 'City is required',
          v => (v || '').length > 2 || `min 3`
        ],
        email: [
          v => !!v || 'E-mail is required',
          v => /.+@.+/.test(v) || 'E-mail must be valid',
        ],
        password: [
          (v) => !!v || 'Password is required',
          v => (v || '').length > 7 || `min 8 `
        ],
        check: [
          (v) => !!v || 'is required',
        ],
        CourtName: [
          (v) => !!v || 'Cour tName is required',
          v => (v || '').length > 2 || `min 3 `
        ],
        CourtCity: [
          (v) => !!v || 'Cour tName is required',
          v => (v || '').length > 1 || `min 2 `
        ],
        CourtAdress: [
          (v) => !!v || 'Cour tName is required',
          v => (v || '').length > 5 || `min 6 `
        ],
        CourtPhone: [
          (v) => !!v || 'Cour tName is required',
          v => (v || '').length > 7 || `min 8 `
        ],
        photo: [
          (v) => !!v || 'is required',
        ],
      }
    }
  },
  methods: {
    changePh(){
      this.form.fileName = document.querySelector('input[type=file]').files[0].name
      
      if (this.$refs.text1.files.length === null) this.image = null
      else {
          this.image = this.$refs.text1.files[0]
      }
    },
    createCourt() {
      if (this.image && this.form.courtName.length > 2)  {
        console.log(this.form.courtName)
        const formData = new FormData()
        formData.append(this.form.courtName, this.image)
        const NA = {
          city: this.form.courtCity,
          adress: this.form.courtAdress,
          phone: this.form.courtPhone,
          name: this.form.courtName
        }
        axios.post('http://82.146.45.20/api/user/upload_photo', NA)
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
        axios.post('http://82.146.45.20/api/user/upload_photo', formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
      }
    },
    login() {
      if (this.$refs.formAuth.validate()) {
        this.$store.dispatch('login', {
          email: this.form.email,
          password: this.form.password,
        }).then(() => {
          this.$router.push('/user')
        }).catch(err => {
          console.log(err)
        })
      }
    },
    register() {
      if (this.$refs.formReg.validate()) {
        this.$store.dispatch('register', {
          name: this.form.firstName +' '+ this.form.lastName,
          city: this.form.city,
          email: this.form.email,
          password: this.form.password,
        }).then(() => {
          this.$router.push('/user')
        }).catch(err => {
          console.log(err)
        })
      }
    },
    clear() {
      this.$refs.form.reset()
    }
  },
  computed: {
    info() {
      return this.$store.state.info
    }
  },
  components: {}
}
</script>
<style >
.label:hover{
  color:blue;
}
</style>
