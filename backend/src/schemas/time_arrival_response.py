from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPTimeArrivalResponse:

    @staticmethod
    def GET_SUCESSFULLY(data_param) -> HttpResponseModel: 
        return HttpResponseModel (
            message="Tempo estimado do produto calculado com sucesso!",
            status_code=201,
            data= data_param
        ) 

    @staticmethod
    def BAD_REQUEST(errors) -> HttpResponseModel:

        return HttpResponseModel (
            message="Informações inválidas", 
            status_code= 400,
            data=["User CEP"]
        )