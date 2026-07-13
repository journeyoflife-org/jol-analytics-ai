"""Unit tests for access control."""

import pytest

from jol_analytics_ai.security.access_control import (
    Permission,
    Role,
    check_access,
    require_access,
)


class TestCheckAccess:
    def test_admin_has_all_permissions(self) -> None:
        for perm in Permission:
            decision = check_access(Role.ADMIN, perm)
            assert decision.allowed is True

    def test_viewer_cannot_train_model(self) -> None:
        decision = check_access(Role.VIEWER, Permission.TRAIN_MODEL)
        assert decision.allowed is False

    def test_data_scientist_can_train(self) -> None:
        decision = check_access(Role.DATA_SCIENTIST, Permission.TRAIN_MODEL)
        assert decision.allowed is True

    def test_viewer_can_read_data(self) -> None:
        decision = check_access(Role.VIEWER, Permission.READ_DATA)
        assert decision.allowed is True


class TestRequireAccess:
    def test_raises_on_denied(self) -> None:
        with pytest.raises(PermissionError):
            require_access(Role.VIEWER, Permission.MANAGE_USERS)

    def test_passes_on_allowed(self) -> None:
        require_access(Role.ADMIN, Permission.MANAGE_USERS)  # should not raise
