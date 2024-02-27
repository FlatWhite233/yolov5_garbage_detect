export interface IListItem {
  avatar?: string
  title: string
  datetime?: string
  description?: string
  status?: "" | "success" | "info" | "warning" | "danger"
  extra?: string
}

export const notifyData: IListItem[] = [
  {
    avatar: "https://gw.alipayobjects.com/zos/rmsportal/OKJXDXrmkNshAMvwtvhu.png",
    title: "GPT-4发布！",
    datetime: "2023-03-15",
    description: "GPT-4 是 OpenAI 最先进的系统，可产生更安全、更有用的响应。"
  },
  {
    avatar: "https://gw.alipayobjects.com/zos/rmsportal/OKJXDXrmkNshAMvwtvhu.png",
    title: "YOLOv5发布！",
    datetime: "2020-06-26",
    description:
      "YOLOv5🚀是全球最受欢迎的视觉AI，代表了Ultralytics对未来视觉AI方法的开源研究，融合了数千小时研究和开发过程中积累的经验教训和最佳实践。"
  }
]

export const messageData: IListItem[] = [
  {
    avatar: "https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png",
    title: "新年快乐！",
    description: "新年快乐！",
    datetime: "2023-01-01"
  },
  {
    avatar: "https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png",
    title: "听你自己的声音",
    description: "外面的世界太嘈杂了，你得听自己的声音",
    datetime: "2022-10-10"
  },
  {
    avatar: "https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png",
    title: "温柔的人会带你离开海底",
    description: "大海的深处贩卖着蓝色的孤独，温柔的人会带你离开海底。",
    datetime: "2021-06-19"
  }
]

export const todoData: IListItem[] = [
  {
    title: "任务名称",
    description: "这家伙很懒，什么都没留下",
    extra: "未开始",
    status: "info"
  },
  {
    title: "任务名称",
    description: "这家伙很懒，什么都没留下",
    extra: "进行中",
    status: ""
  },
  {
    title: "任务名称",
    description: "这家伙很懒，什么都没留下",
    extra: "已超时",
    status: "danger"
  }
]
