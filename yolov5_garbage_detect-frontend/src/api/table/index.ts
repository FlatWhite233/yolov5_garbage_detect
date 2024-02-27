import { request } from "@/utils/service"
import type * as Table from "./types/table"

/** 增 */
export function createTableDataApi(data: Table.ICreateTableRequestData) {
  return request<Table.createTableResponseData>({
    url: "table/add",
    // url: "table",
    method: "post",
    data
  })
}

/** 删 */
export function deleteTableDataApi(id: string) {
  return request<Table.deleteTableResponseData>({
    url: `table/delete/${id}`,
    // url: `table/${id}`,
    method: "delete"
  })
}

/** 改 */
export function updateTableDataApi(data: Table.IUpdateTableRequestData) {
  return request<Table.upDateTableResponseData>({
    url: "table/update",
    // url: "table",
    method: "put",
    data
  })
}

/** 查 */
export function getTableDataApi(params: Table.IGetTableRequestData) {
  return request<Table.GetTableResponseData>({
    url: "table/list",
    // url: "table",
    method: "get",
    params
  })
}
