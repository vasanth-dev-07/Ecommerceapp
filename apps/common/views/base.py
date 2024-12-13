from rest_framework import permissions, status
from rest_framework.response import Response


class NonAuthenticatedApiMixin:
    """this mixin is used to give all type of permission to the API"""

    permission_class = [permissions.AllowAny]


class CommonViewMixin:
    # this base view mixin contains common function

    def get_request(self):
        # returns request
        return self.request

    def get_user(self):
        """Returns User"""

        return self.get_request().user

    def get_authenticated_user(self):
        """Returns the authenticated user."""

        user = self.get_user()
        return user if user and user.is_authenticated else None

    def send_error_response(self,data=None):
        """Common function to send error message"""

        return self.send_response(data=data,status_code = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def send_response(
            data = None,
            status_code = status.HTTP_200_OK,
            action_code = "Do nothing",
            **other_response_data
    ):
        return Response(
            data={
                "data": data,
                "status": "success" if status.is_success(status_code) else "error",
                "action": action_code,
                **other_response_data,
            },
            status=status_code,
        )









