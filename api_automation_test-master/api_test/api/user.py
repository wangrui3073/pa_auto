import re

from rest_framework import parsers, renderers
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView

from api_test.serializers import TokenSerializer
from api_test.common.api_response import JsonResponse


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        用户登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # token, created = Token.objects.get_or_create(user=user)
        data = TokenSerializer(Token.objects.get(user=user)).data
        data["userphoto"] = '/file/userphoto.jpg'
        return JsonResponse(data=data, code="999999", msg="成功")


obtain_auth_token = ObtainAuthToken.as_view()

# 修改密码
class PwdView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def post(self, request):
        # 1.接收
        old_pwd = request.POST.get('old_pwd')
        new_pwd = request.POST.get('new_pwd')
        new_cpwd = request.POST.get('new_cpwd')
        # 2.验证旧密码是否正确
        user = request.user
        if not user.check_password(old_pwd):
            return JsonResponse(code="999996", msg="旧密码错误")
        if not re.match('^[0-9A-Za-z]{8,20}$', new_pwd):
            return JsonResponse(code="999996", msg="密码为8-20个字符")
        # 3.确认密码
        if new_pwd != new_cpwd:
            return JsonResponse(code="999996", msg="两个密码不一致")
        # 4.保存新密码
        user.set_password(new_pwd)
        user.save()
        # 5.响应
        return JsonResponse(code="999999", msg="成功")
