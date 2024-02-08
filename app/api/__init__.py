from fastapi import APIRouter

from app.api.auth.auth_register import auth_register
from app.api.auth.auth_login import auth_login, LoginResponseModel
from app.api.auth.auth_logout import auth_logout
from app.api.auth.auth_refresh_token import auth_refresh_token, RefreshTokenResponseModel
from app.api.auth.get_profile import get_users
from app.api.auth.getUser_byID import getUser_byID
from app.api.auth.updateUser import updateUser

from app.api.gudang.tambah_gudang import tambah_gudang
from app.api.gudang.get_gudang import get_gudang
from app.api.gudang.getGudang_byID import getGudang_byID
from app.api.gudang.updateGudang import updateGudang

from app.api.kategori.tambah_kategori import tambah_kategori
from app.api.kategori.get_kategori import get_kategori
from app.api.kategori.getKategori_byID import getKategori_byID
from app.api.kategori.updateKategori import updateKategori

from app.api.produk.tambah_produk import tambah_produk
from app.api.produk.get_produk import get_produk
from app.api.produk.getProduk_byID import getProduk_byID
from app.api.produk.updateProduk import updateProduk

from app.api.rak.tambah_rak import tambah_rak
from app.api.rak.get_rak import get_rak
from app.api.rak.getRak_byID import getRak_byID
from app.api.rak.updateRak import updateRak

from app.api.satuan.tambah_satuan import tambah_satuan
from app.api.satuan.get_satuan import get_satuan
from app.api.satuan.getSatuan_byID import getSatuan_byID
from app.api.satuan.updateSatuan import updateSatuan


api_router = APIRouter()

api_router.add_api_route('/api/auth/register', auth_register, methods=['POST'], tags=['Auth'], status_code=201)
api_router.add_api_route('/api/auth/login', auth_login,methods=['POST'], tags=['Auth'], response_model=LoginResponseModel)
api_router.add_api_route('/api/auth/logout', auth_logout,methods=['POST'], tags=['Auth'], status_code=204)
# api_router.add_api_route('/api/v1/auth/refresh-token', auth_refresh_token,methods=['POST'], tags=['Auth'], response_model=RefreshTokenResponseModel)
api_router.add_api_route('/api/auth/get-users', get_users,methods=['GET'], tags=['Auth'], status_code=200)
api_router.add_api_route('/api/auth/get-user/{user_id}', getUser_byID, methods=['GET'], tags=['Auth'], status_code=200)
api_router.add_api_route('/api/auth/update-user/{user_id}', updateUser, methods=['PUT'], tags=['Auth'], status_code=200)

api_router.add_api_route('/api/tambah-gudang', tambah_gudang,methods=['POST'], tags=['Gudang'], status_code=201)
api_router.add_api_route('/api/get-gudang', get_gudang,methods=['GET'], tags=['Gudang'], status_code=200)
api_router.add_api_route('/api/get-gudang/{gudang_id}', getGudang_byID, methods=['GET'], tags=['Gudang'], status_code=200)
api_router.add_api_route('/api/auth/update-gudang/{gudang_id}', updateGudang, methods=['PUT'], tags=['Gudang'], status_code=200)

api_router.add_api_route('/api/tambah-kategori', tambah_kategori,methods=['POST'], tags=['Kategori'], status_code=201)
api_router.add_api_route('/api/get-kategori', get_kategori,methods=['GET'], tags=['Kategori'], status_code=200)
api_router.add_api_route('/api/get-kategori/{kategori_id}', getKategori_byID, methods=['GET'], tags=['Kategori'], status_code=200)
api_router.add_api_route('/api/auth/update-kategori/{kategori_id}', updateKategori, methods=['PUT'], tags=['Kategori'], status_code=200)

api_router.add_api_route('/api/tambah-produk', tambah_produk,methods=['POST'], tags=['Produk'], status_code=201)
api_router.add_api_route('/api/get-produk', get_produk,methods=['GET'], tags=['Produk'], status_code=200)
api_router.add_api_route('/api/get-produk/{produk_id}', getProduk_byID, methods=['GET'], tags=['Produk'], status_code=200)
api_router.add_api_route('/api/update-produk/{produk_id}', updateProduk, methods=['PUT'], tags=['Produk'], status_code=200)

api_router.add_api_route('/api/tambah-rak', tambah_rak,methods=['POST'], tags=['Rak'], status_code=201)
api_router.add_api_route('/api/get-rak', get_rak,methods=['GET'], tags=['Rak'], status_code=200)
api_router.add_api_route('/api/get-rak/{rak_id}', getRak_byID, methods=['GET'], tags=['Rak'], status_code=200)
api_router.add_api_route('/api/update-rak/{rak_id}', updateRak, methods=['PUT'], tags=['Rak'], status_code=200)

api_router.add_api_route('/api/tambah-satuan', tambah_satuan,methods=['POST'], tags=['Satuan'], status_code=201)
api_router.add_api_route('/api/get-satuan', get_satuan,methods=['GET'], tags=['Satuan'], status_code=200)
api_router.add_api_route('/api/get-satuan/{satuan_id}', getSatuan_byID, methods=['GET'], tags=['Satuan'], status_code=200)
api_router.add_api_route('/api/update-satuan/{satuan_id}', updateSatuan, methods=['PUT'], tags=['Satuan'], status_code=200)
