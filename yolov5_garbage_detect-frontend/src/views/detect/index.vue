<script lang="ts" setup>
import { computed, reactive, ref } from "vue"
import { type IWeightsData } from "@/api/detect/types/detect"
import { Refresh } from "@element-plus/icons-vue"
import { getAllEnableWeightsApi, getCurrentWeightsApi, switchWeightsApi } from "@/api/detect"
import { ElMessage } from "element-plus"
import UploadFile from "@/components/UploadFile/index.vue"

defineOptions({
  name: "Detect"
})

const loading = ref<boolean>(false)
const weightsData = ref<IWeightsData[]>([])
const selectedOptions = ref([])
const options = ref<{ value: string; label: string; children: { value: string; label: string }[] }[]>([])
// 当前选择模型数据
const currentWeightsData = reactive({
  weightsName: "",
  weightsVersion: ""
})
// 绑定下拉选项数据
const selectedWeightsData = reactive({
  weightsName: "",
  weightsVersion: ""
})
// 检测结果图片
// base64解码
const detectImageData: any = reactive({
  originalBase64: "",
  resultBase64: "",
  originalImageUrl: computed(() => {
    if (detectImageData.originalBase64) {
      const blob = dataURItoBlob(detectImageData.originalBase64)
      return URL.createObjectURL(blob)
    } else {
      return ""
    }
  }),
  resultImageUrl: computed(() => {
    if (detectImageData.resultBase64) {
      const blob = dataURItoBlob(detectImageData.resultBase64)
      return URL.createObjectURL(blob)
    } else {
      return ""
    }
  }),
  detectResult: []
})
// 处理上传文件
const onHandleUpload = (res: any) => {
  // 如果后端的数据没有以 data:image/jpeg;base64 则需要判断加上
  const originalBase64 = res.data.originalBase64
  const resultBase64 = res.data.resultBase64
  detectImageData.detectResult = res.data.detectResult
  const base64Prefix = "data:image/jpeg;base64,"
  // 判断 originalBase64 是否以 base64Prefix 开头，如果没有则加上
  if (!originalBase64.startsWith(base64Prefix)) {
    detectImageData.originalBase64 = base64Prefix + originalBase64
  } else {
    detectImageData.originalBase64 = originalBase64
  }
  // 判断 resultBase64 是否以 base64Prefix 开头，如果没有则加上
  if (!resultBase64.startsWith(base64Prefix)) {
    detectImageData.resultBase64 = base64Prefix + resultBase64
  } else {
    detectImageData.resultBase64 = resultBase64
  }
}
// 图片base64解码
const dataURItoBlob = (dataURI: any) => {
  const byteString = atob(dataURI.split(",")[1])
  const mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0]
  const ab = new ArrayBuffer(byteString.length)
  const ia = new Uint8Array(ab)
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i)
  }
  return new Blob([ab], { type: mimeString })
}
/** 获取所有可调用权重 */
const getAllEnableWeights = () => {
  loading.value = true
  getAllEnableWeightsApi()
    .then((res) => {
      weightsData.value = res.data.list
      options.value = generateCascaderOptions(res.data.list)
    })
    .catch(() => {
      weightsData.value = []
    })
    .finally(() => {
      loading.value = false
    })
}
/** 获取当前调用权重 */
const getCurrentWeights = () => {
  getCurrentWeightsApi().then((res) => {
    currentWeightsData.weightsName = res.data.weightsName
    currentWeightsData.weightsVersion = res.data.weightsVersion
  })
}
// 生成下拉菜单的选项
const generateCascaderOptions = (list: IWeightsData[]) => {
  const options: { value: string; label: string; children: { value: string; label: string }[] }[] = []
  const map: { [key: string]: { value: string; label: string; children: { value: string; label: string }[] } } = {}
  list.forEach((item) => {
    const version = item.weightsVersion
    const name = item.weightsName
    if (!map[version]) {
      map[version] = {
        value: version,
        label: version,
        children: []
      }
      options.push(map[version])
    }
    map[version].children.push({
      value: name,
      label: name
    })
  })
  return options
}
// 下拉菜单的选择事件
const handleChange = (selectedOptions: string[]) => {
  if (selectedOptions.length !== 2) return // 如果选中的项数不为2，则返回
  selectedWeightsData.weightsName = selectedOptions[1]
  selectedWeightsData.weightsVersion = selectedOptions[0]
  const message = `已选择模型：${selectedOptions[1]} 模型版本：${selectedOptions[0]}`
  ElMessage({
    message: message,
    type: "success"
  })
}
// 下拉菜单的展开方式
interface CascaderProps {
  expandTrigger?: "click" | "hover"
}
const props: CascaderProps = {
  expandTrigger: "hover" as const
}
// 切换模型
const handleSwitch = () => {
  if (
    selectedWeightsData.weightsName === currentWeightsData.weightsName &&
    selectedWeightsData.weightsVersion === currentWeightsData.weightsVersion
  ) {
    ElMessage({
      message: "当前调用的已经是该模型",
      type: "warning"
    })
    return
  } else if (selectedWeightsData.weightsName === "" || selectedWeightsData.weightsVersion === "") {
    ElMessage({
      message: "请先选择模型",
      type: "warning"
    })
    return
  }
  switchWeightsApi({
    switchWeightsName: selectedWeightsData.weightsName,
    switchWeightsVersion: selectedWeightsData.weightsVersion
  }).then(() => {
    getCurrentWeights()
  })
}
getCurrentWeights()
getAllEnableWeights()
</script>

<template>
  <div class="app-container">
    <el-card v-loading="loading" shadow="never" class="search-wrapper">
      <el-row>
        <el-col :span="7">
          <div class="grid-content">
            <div>
              <div class="SwitchModelCSS">
                当前调用模型：
                <el-text v-model="currentWeightsData.weightsName" type="success" size="large">
                  {{ currentWeightsData.weightsName }}
                </el-text>
              </div>
              <div class="SwitchModelCSS">
                当前模型版本：
                <el-text v-model="currentWeightsData.weightsVersion" type="success" size="large">
                  {{ currentWeightsData.weightsVersion }}
                </el-text>
              </div>
            </div>
          </div>
        </el-col>
        <el-col :span="3" class="SwitchModelCSS"> 选择其他模型： </el-col>
        <el-col :span="4">
          <div class="m-4">
            <el-cascader
              v-model="selectedOptions"
              :options="options"
              :props="props"
              @change="handleChange"
              placeholder="请选择模型"
            />
          </div>
        </el-col>
        <el-col :span="4" class="SwitchModelCSS">
          <div class="grid-content ep-bg-purple">
            <el-button type="success" :icon="Refresh" @click="handleSwitch">切换模型</el-button>
          </div>
        </el-col>
      </el-row>
    </el-card>
    <el-card v-loading="loading" shadow="never" class="search-wrapper">
      <UploadFile @handleUpload="onHandleUpload" />
    </el-card>
    <el-card v-loading="loading" shadow="never" class="search-wrapper">
      <el-row :gutter="20">
        <el-col :span="10">
          <div class="grid-content ep-bg-purple">
            <el-image
              v-if="detectImageData.originalBase64"
              :src="detectImageData.originalImageUrl"
              :fit="'scaleDown'"
              :preview-src-list="[detectImageData.originalImageUrl]"
            />
            <div v-else class="image-placeholder">原始图片</div>
          </div>
        </el-col>
        <el-col :span="10">
          <div class="grid-content ep-bg-purple">
            <el-image
              v-if="detectImageData.resultBase64"
              :src="detectImageData.resultImageUrl"
              :fit="'scaleDown'"
              :preview-src-list="[detectImageData.resultImageUrl]"
            />
            <div v-else class="image-placeholder">检测结果图片</div>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content ep-bg-purple">
            <el-table
              :data="detectImageData.detectResult"
              v-if="detectImageData.detectResult && detectImageData.detectResult.length > 0"
            >
              <el-table-column prop="className" label="检测类别" />
              <el-table-column prop="confidence" label="置信度" />
            </el-table>
            <div v-else class="image-placeholder">暂无结果</div>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<style lang="scss" scoped>
.image-placeholder {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 300px;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 15px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.SwitchModelCSS {
  display: flex;
  font-size: 15px;
  font-weight: 500;
  padding: 5px;
  justify-content: flex-start;
  align-items: center;
}
.search-wrapper {
  margin-bottom: 20px;
  :deep(.el-card__body) {
    padding-bottom: 15px;
  }
}
.toolbar-wrapper {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.table-wrapper {
  margin-bottom: 20px;
}
.pager-wrapper {
  display: flex;
  justify-content: flex-end;
}
</style>
