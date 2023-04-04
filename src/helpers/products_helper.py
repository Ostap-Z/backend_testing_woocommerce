import allure

from src.utilities.requests_utility import RequestsUtility


class ProductsHelper:

    def __init__(self):
        self.request_utility = RequestsUtility()

    def get_product_by_id(
            self,
            product_id
    ):
        with allure.step(
            f"Get a specific product with id: {product_id}"
        ):
            return self.request_utility.get(f"products/{product_id}")

    def create_product(
            self,
            payload
    ):
        with allure.step(
                "Create product with data: "
                f"endpoint='products', {payload=}"
        ):
            return self.request_utility.post(
                "products",
                payload=payload,
                expected_status_code=201
            )

    def get_products_with_params(
            self,
            payload=None,
            max_pages=100
    ):
        all_products = []

        for i in range(1, max_pages + 1):
            if "per_page" not in payload.keys():
                payload["per_page"] = 100
            payload["page"] = i
            api_response = self.request_utility.get(
                "products",
                payload=payload
            )
            if not api_response:
                break
            else:
                all_products.extend(api_response)
        else:
            raise Exception(
                f"Unable to find all products after {max_pages} pages"
            )

        with allure.step(
            "Get a products list with params from API: "
            f"{payload=}, {max_pages=}"
        ):
            return all_products

    def update_product(
        self,
        product_id,
        payload
    ):
        with allure.step(
            f"Update the product {product_id} with payload: {payload}"
        ):
            return self.request_utility.put(
                endpoint=f"products/{product_id}",
                payload=payload
            )
