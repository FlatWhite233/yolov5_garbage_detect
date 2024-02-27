<script setup lang="ts">
import { UploadFilled } from "@element-plus/icons-vue"
import { ElMessage } from "element-plus"

const emits = defineEmits(["handleUpload"])
const handleUpload = (response: any) => {
  const code = response.code
  const message = response.message
  if (code === 0) {
    ElMessage.success(message)
  } else {
    ElMessage.error(message)
  }
  emits("handleUpload", response) // 触发自定义事件，并将 response 作为参数传递
}
</script>
<template>
  <el-upload
    class="upload-demo"
    drag
    action="http://localhost:3333/api/v1/detect/upload"
    :on-success="handleUpload"
    multiple
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">将需要检测的图片拖放到此处或<em>点击上传</em></div>
    <template #tip>
      <div class="el-upload__tip">图片格式仅支持jpg/png</div>
    </template>
  </el-upload>
</template>

<style lang="scss" scoped></style>
