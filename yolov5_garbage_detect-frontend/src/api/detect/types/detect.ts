export interface IWeightsData {
  weightsName: string
  weightsVersion: string
}

export interface ISwitchRoleRequestData {
  switchWeightsName: string
  switchWeightsVersion: string
}

export type GetEnableWeightsResponseData = IApiResponseData<{ list: IWeightsData[] }>

export type GetCurrentWeightsResponseData = IApiResponseData<IWeightsData>

export type SwitchWeightsResponseData = IApiResponseData<IWeightsData>
