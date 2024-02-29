import requests


class GETUnsplashImg:
    query = ""
    unsplash_application_id = r"572011"
    unsplash_access_key = r"SScWIK8xwYoxWFdNNMDMcMepcYdpe-rRIvWrPz_6YM4"
    unsplash_secret_key = r"u5gw-3J3Tkdf5F0VGDnRfBFWIR1B0Xufn-JmvgsMZPI"

    def getUrl(self, img):
        url = f"https://api.unsplash.com/search/photos?query={str(img)}&client_id={self.unsplash_access_key}"
        response = requests.get(url)
        content = response.json()
        urls = content["results"][0]["urls"]["regular"]
        return urls


if __name__ == "__main__":
    url = GETUnsplashImg().getUrl("food")
    print(url)
    print(len(url))
