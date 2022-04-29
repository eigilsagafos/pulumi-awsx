# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-awsx. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'NatGatewayStrategy',
    'SubnetType',
]


class NatGatewayStrategy(str, Enum):
    """
    A strategy for creating NAT Gateways for private subnets within a VPC.
    """
    NONE = "None"
    """
    Do not create any NAT Gateways. Resources in private subnets will not be able to access the internet.
    """
    SINGLE = "Single"
    """
    Create a single NAT Gateway for the entire VPC. This configuration is not recommended for production infrastructure as it creates a single point of failure.
    """
    ONE_PER_AZ = "OnePerAz"
    """
    Create a NAT Gateway in each availability zone. This is the recommended configuration for production infrastructure.
    """


class SubnetType(str, Enum):
    """
    A type of subnet within a VPC.
    """
    PUBLIC = "Public"
    """
    A subnet whose hosts can directly communicate with the internet.
    """
    PRIVATE = "Private"
    """
    A subnet whose hosts can not directly communicate with the internet, but can initiate outbound network traffic via a NAT Gateway.
    """
    ISOLATED = "Isolated"
    """
    A subnet whose hosts have no connectivity with the internet.
    """