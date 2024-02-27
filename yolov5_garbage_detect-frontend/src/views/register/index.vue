<script lang="ts" setup>
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"
import { useUserStore } from "@/store/modules/user"
import { User, Lock, Key, Message } from "@element-plus/icons-vue"
import ThemeSwitch from "@/components/ThemeSwitch/index.vue"
import { type FormInstance, FormRules } from "element-plus"
import { getRegisterCodeApi } from "@/api/register"
import { type IRegisterRequestData } from "@/api/register/types/register"

const router = useRouter()
const registerFormRef = ref<FormInstance | null>(null)

/** 登录按钮 Loading */
const loading = ref(false)
/** 验证码按钮 Disable */
const captchaButtonDisable = ref(false)

/** 注册表单数据 */
const registerForm: IRegisterRequestData = reactive({
  username: "",
  email: "",
  password: "",
  confirm_password: "",
  captcha: ""
})
/** 验证两次密码是否一致 */
const validateConfirmPassword = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请再次输入密码"))
  } else if (value !== registerForm.password) {
    callback(new Error("两次密码输入不一致"))
  } else {
    callback()
  }
}
/** 注册表单校验规则 */
const registerFormRules: FormRules = {
  username: [
    { required: true, message: "请输入用户名", trigger: "blur" },
    { min: 2, max: 20, message: "长度在 2 到 20 个字符", trigger: "blur" }
  ],
  email: [
    { required: true, message: "请输入邮箱", trigger: "blur" },
    { type: "email", message: "请输入正确的邮箱格式", trigger: "change" }
  ],
  password: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 4, max: 20, message: "长度在 4 到 20 个字符", trigger: "blur" }
  ],
  confirm_password: [{ required: true, validator: validateConfirmPassword, trigger: "blur" }],
  captcha: [{ required: true, message: "请输入验证码", trigger: "blur" }]
}
/** 登录逻辑 */
const handleLogin = () => {
  router.push({ path: "/login" })
}
/** 获取验证码 */
const captchaButtonText = ref("获取验证码")
const getCaptcha = () => {
  const email = registerForm.email
  if (registerForm.email !== "") {
    getRegisterCodeApi(email).then((res: any) => {
      const code = res.code
      if (code === 200) {
        captchaButtonDisable.value = true
        captchaButtonText.value = "验证码已发送"
      } else {
        captchaButtonDisable.value = false
        captchaButtonText.value = "获取验证码"
        registerForm.email = ""
      }
    })
  } else {
    getRegisterCodeApi(email)
    captchaButtonDisable.value = false
    captchaButtonText.value = "获取验证码"
  }
}
/** 创建验证码 */
const createCode = () => {
  // 先清空验证码的输入
  registerForm.captcha = ""
}
/** 初始化验证码 */
createCode()

const handleRegister = () => {
  registerFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      loading.value = true
      useUserStore()
        .register({
          username: registerForm.username,
          email: registerForm.email,
          password: registerForm.password,
          confirm_password: registerForm.confirm_password,
          captcha: registerForm.captcha
        })
        .then(() => {
          router.push({ path: "/login" })
        })
        .catch(() => {
          createCode()
          registerForm.username = ""
          registerForm.email = ""
          registerForm.password = ""
        })
        .finally(() => {
          loading.value = false
        })
    } else {
      return false
    }
  })
}
</script>

<template>
  <div class="login-container">
    <ThemeSwitch class="theme-switch" />
    <div class="login-card">
      <div class="title">
        <img src="@/assets/layout/logo-text-2.png" />
      </div>
      <div class="content">
        <el-form ref="registerFormRef" :model="registerForm" :rules="registerFormRules" @keyup.enter="handleRegister">
          <el-form-item prop="email">
            <el-input
              v-model.trim="registerForm.email"
              placeholder="邮箱"
              type="text"
              tabindex="0"
              :prefix-icon="Message"
              size="large"
            />
          </el-form-item>
          <el-form-item prop="username">
            <el-input
              v-model.trim="registerForm.username"
              placeholder="用户名"
              type="text"
              tabindex="1"
              :prefix-icon="User"
              size="large"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model.trim="registerForm.password"
              placeholder="密码"
              type="password"
              tabindex="2"
              :prefix-icon="Lock"
              size="large"
              show-password
            />
          </el-form-item>
          <el-form-item prop="confirm_password">
            <el-input
              v-model.trim="registerForm.confirm_password"
              placeholder="确认密码"
              type="password"
              tabindex="2"
              :prefix-icon="Lock"
              size="large"
              show-password
            />
          </el-form-item>
          <el-form-item prop="code">
            <el-input
              v-model.trim="registerForm.captcha"
              placeholder="验证码"
              type="text"
              tabindex="3"
              :prefix-icon="Key"
              maxlength="7"
              size="large"
            >
              <template #suffix>
                <el-button
                  style="margin-top: 0 !important"
                  type="primary"
                  text
                  @click="getCaptcha"
                  :disabled="captchaButtonDisable"
                >
                  {{ captchaButtonText }}
                </el-button>
              </template>
            </el-input>
          </el-form-item>
          <div style="width: 48%; display: inline-block">
            <el-button :loading="loading" type="success" size="default" @click.prevent="handleLogin"> 登 录 </el-button>
          </div>
          <div style="width: 4%; display: inline-block" />
          <div style="width: 48%; display: inline-block">
            <el-button :loading="loading" type="primary" size="default" @click.prevent="handleRegister">
              注 册
            </el-button>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100%;
  .theme-switch {
    position: fixed;
    top: 5%;
    right: 5%;
    cursor: pointer;
  }
  .login-card {
    width: 480px;
    border-radius: 20px;
    box-shadow: 0 0 10px #dcdfe6;
    background-color: #fff;
    overflow: hidden;
    .title {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 150px;
      img {
        height: 100%;
      }
    }
    .content {
      padding: 20px 50px 50px 50px;
      :deep(.el-input-group__append) {
        padding: 0;
        overflow: hidden;
        .el-image {
          width: 100px;
          height: 40px;
          border-left: 0px;
          user-select: none;
          cursor: pointer;
          text-align: center;
        }
      }
      .el-button {
        width: 100%;
        margin-top: 10px;
      }
    }
  }
}
</style>
